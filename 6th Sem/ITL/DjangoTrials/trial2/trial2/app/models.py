from django.db import models

SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

class Category(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    numberOfVisits = models.IntegerField()
    numberOfLikes = models.IntegerField()
    car = models.CharField(max_length=100,choices=SEMESTER_CHOICES)