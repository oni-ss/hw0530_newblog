from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', default='static/mariahcarey_emc2.png')
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]