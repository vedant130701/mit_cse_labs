from django.shortcuts import render
from .models import Works,Lives
from .forms import Employee,Company

def index(request):
    return render(request,'index.html')

def portal(request):
    form1 = Employee()
    form = Employee(request.POST)
    if form.is_valid():
        Name = form.cleaned_data['Name']
        Company = form.cleaned_data['Company']
        Salary = form.cleaned_data['Salary']
        Street = form.cleaned_data['Street']
        City = form.cleaned_data['City']
        Works.objects.create(Name=Name,Company=Company,Salary=Salary)
        Lives.objects.create(Name=Name,Street=Street,City=City)
    return render(request,'portal.html',{"form":form1})

def search(request):
    form1 = Company()
    form = Company(request.POST)
    if form.is_valid():
        company = form.cleaned_data["company"]
        employall = Works.objects.all().filter(Company = company)
        employees = []
        for e in employall:
            employees.append(Lives.objects.get(Name = e.Name))
        return render(request,"search.html",{"form":form,"employees":employees})
    return render(request,"search.html",{"form":form1})