from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date=models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:200]
    def sdate(self):
        return self.pub_date.strftime(' %b %e %Y')
