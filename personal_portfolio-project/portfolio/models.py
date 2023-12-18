from django.db import models

# necessery step 
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)   # dont necessery need for user, so its optional

    # adding this function so in /admin insted of Project object(n) it displays the name of the object
    def __str__(self):
        return self.title
    