from django.db import models

class Blog(models.Model):
    b_title = models.CharField(max_length=255)
    a_name = models.CharField(max_length=50)
    b_image=models.ImageField(upload_to='blog_image',default="default.jpg")
    b_content=models.TextField(default='')
    pub_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.b_title
