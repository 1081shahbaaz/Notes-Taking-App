from django.shortcuts import render,redirect

from notesapp.forms import UpdateProfileForm, UpdateUserForm
from .models import Document
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@login_required(login_url='/login/')
def editor(request):
    docid = int(request.GET.get('docid',0))
    documents = Document.objects.filter(user=request.user)
    # documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')



        if docid>0:
            # if request.user.is_authenticated:
                document = Document.objects.get(pk=docid,user=request.user)
                document.title = title.capitalize()
                document.content = content
                document.save()

                return redirect('/?docid=%i' % docid)
            # else:
                return redirect('login')


        else:

            # if not request.user.is_authenticated:
            #     return redirect('login')
            
            # else:
            document = Document.objects.create(title=title.capitalize(),content=content,user=request.user)
            return redirect('/?docid=%i' % document.id)



    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document' : document,

    }

    return render(request,'editor.html',context)
@login_required(login_url='/login/')
def delete_document(request, docid):
    document = Document.objects.get(pk=docid,user=request.user)
    # document = Document.objects.get(pk=docid)
    # if request.user.is_authenticated:
    document.delete()
    return redirect('/?docid=0')
    # else:
    #     return redirect('login')



def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if first_name == '' or last_name == '' or username == '' or email == '' or password1 == '' or password2 == '':
            messages.error(request,'Please fill all the Credentials')
            return render(request,'register.html')

        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return render(request,'register.html')
            else:

                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return render(request,'register.html')

    return render(request,'register.html')

def loginview(request):

    valuenext= request.POST.get('next')
    # print('****')
    # print(valuenext)
    # print('****')


    if request.method == 'POST':
        # import pdb; pdb.set_trace()

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == '' or password == '':
            messages.info(request,'Please fill the credentials')
            return render(request,'login.html')
        else:

            user = authenticate(request, username=username,password=password)
        

            if user is not None and valuenext == '':
                login(request, user)
                return redirect('editor')

            if user is not None and valuenext != '':
                login(request, user)
                return redirect(valuenext)
            else:
                messages.info(request,'invalid credentials')  
                return render(request,'login.html')

    else:
        return render(request,'login.html')

@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def profile(request):
#    Profile.objects.get_or_create(user=request.user)
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html',{'user_form':user_form,'profile_form':profile_form})




  


