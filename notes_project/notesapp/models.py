from django.db import models
from django.contrib.auth.models import User 

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
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title.upper()
