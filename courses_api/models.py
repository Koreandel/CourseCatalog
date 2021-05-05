from django.db import models


class Course(models.Model):
    
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    lecture_quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
