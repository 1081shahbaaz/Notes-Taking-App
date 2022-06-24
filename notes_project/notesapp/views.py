from django.shortcuts import render,redirect
from .models import Document
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def editor(request):
    docid = int(request.GET.get('docid',0))
    documents = Document.objects.filter(user=request.user)
    # documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')



        if docid>0:
            if request.user.is_authenticated:
                document = Document.objects.get(pk=docid,user=request.user)
                document.title = title.capitalize()
                document.content = content
                document.save()

                return redirect('/editor?docid=%i' % docid)
            else:
                return redirect('login')


        else:

            if not request.user.is_authenticated:
                return redirect('login')
            
            else:
                document = Document.objects.create(title=title.capitalize(),content=content,user=request.user)
                return redirect('/editor?docid=%i' % document.id)



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
@login_required
def delete_document(request, docid):
    document = Document.objects.get(pk=docid,user=request.user)
    # document = Document.objects.get(pk=docid)
    if request.user.is_authenticated:
        document.delete()
        return redirect('/editor?docid=0')
    else:
        return redirect('login')



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
    if request.method == 'POST':
        # import pdb; pdb.set_trace()

        username = request.POST.get('username')
        password = request.POST.get('password')
        

        if username == '' or password == '':
            messages.info(request,'Please fill the credentials')
            return render(request,'login.html')
        else:

            user = authenticate(request, username=username,password=password)
        

            if user is not None:
                login(request, user)
                return redirect('editor')
            else:
                messages.info(request,'invalid credentials')  
                return render(request,'login.html')

    else:
        return render(request,'login.html')


def logoutview(request):
    logout(request)
    return redirect('login')


