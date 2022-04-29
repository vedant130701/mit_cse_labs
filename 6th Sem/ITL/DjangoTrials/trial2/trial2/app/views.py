from django.shortcuts import render
from .forms import CategoryForm
from .models import Category

def category(request):
    form1 = CategoryForm()
    form = CategoryForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["Name"]
        nov = form.cleaned_data["Number_Of_Visits"]
        nol = form.cleaned_data["Number_Of_Likes"]
        car = form.cleaned_data["Car"]
        Category.objects.create(name = name, numberOfVisits = nov,numberOfLikes = nol, car = car)
        print(name,nov,nol,car)
    return render(request,'category.html',{"form":form1})

def result(request):
    categories = Category.objects.all()
    return render(request,'result.html',{"categories":categories})