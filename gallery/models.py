from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=30,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

    def save_image(self):
        self.save()    

