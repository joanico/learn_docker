from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
        
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    