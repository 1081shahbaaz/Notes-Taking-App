from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, default=1,
                       on_delete= models.CASCADE)  #here
    

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user','title')           # here
        ordering = ('created_at',)

    def __str__(self) -> str:
        return self.title.upper()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpeg', upload_to='Profile_images')
    bio = models.TextField()

    


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):

        super().save()
    

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


    
    







