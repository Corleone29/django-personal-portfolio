from django.db import models

# necessery step 
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # adding this function so in /admin insted of Blog object(n) it displays the name of the object
    def __str__(self):
        return self.title