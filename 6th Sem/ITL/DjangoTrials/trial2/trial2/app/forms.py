from django import forms

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

class CategoryForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Number_Of_Visits = forms.IntegerField()
    Number_Of_Likes = forms.IntegerField()
    Car = forms.ChoiceField(choices=SEMESTER_CHOICES)
