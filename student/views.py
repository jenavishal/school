from django.shortcuts import render
from django.http import HttpResponse
from . models import stud

# Create your views here.
def index(request):
    students = stud.objects.all()    #fetches info from database
    context = {'students': students}
    return render(request, 'index.html', context)

def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        sem = request.POST.get("sem")     #to get post value
        s = stud(naam=name, roll=int(roll), sem=int(sem))
        try:
            s.save()
        except:
            return HttpResponse("roll no already exists")
        return HttpResponse("Your form has been submitted")
    else:
        return render(request, 'create.html')