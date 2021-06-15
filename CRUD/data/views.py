from django.shortcuts import render

# Create your views here.
from data.models import fruit
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect

def home(request):
    fruits = fruit.objects.all().order_by('no')
    if request.method == 'POST':
        request.POST.get('no')
        f=fruit.objects.get(no=request.POST.get('no')[6:])
        f.delete()
        return render(request, 'home.html', {'fruits': fruits})
    return render(request, 'home.html', {'fruits': fruits})

def add(request: HttpRequest) -> HttpResponse:
    condition = {}
    if request.method == 'POST':
        fruitname = request.POST.get('name')
        if fruitname:
            fruit1 = fruit.objects.create(name = fruitname)
            fruit1.save()
            condition = {'condition': 'success'}
            return render(request, 'addfruit.html', condition)
        else:
            condition = {'condition': 'Please Repeat'}
            return render(request, 'addfruit.html', condition)
    return render(request, 'addfruit.html', condition)