from django.shortcuts import render,redirect
from .models import Orbituaries
from datetime import datetime

# Create your views here.
def Home(request):
    return render(request, 'orbituaries/home.html')
def SubmitOrbituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        orbituary = Orbituaries(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death,
                                 content=content, author=author,submission_date=datetime.now())
        orbituary.save()
        return redirect('viewOrbituaries')
    else:
        return render(request, 'orbituaries/orbituaryForm.html')
    
def ViewOrbituaries(request):
    orbituaries = Orbituaries.objects.all()
    return render(request, 'orbituaries/viewOrbituaries.html', {'orbituaries':orbituaries})
