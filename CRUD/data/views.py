from django.shortcuts import render

# Create your views here.
from data.models import fruit
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        request.POST.get('no')
        f=fruit.objects.get(no=request.POST.get('no'))
        f.delete()
    fruits = fruit.objects.all().order_by('no')
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

def edit(request:HttpRequest) -> HttpResponse:
    fruit1 = fruit.objects.get(no=request.GET['no'])
    if 'no' in request.GET and request.method != 'POST':
        #print(request.GET['no'])
        #print(fruit1.name)
        return render(request, 'editfruit.html', locals())
    elif request.method == 'POST':
        re_name = request.POST['name']
        #print(re_name)
        fruit1.name = re_name
        fruit1.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')