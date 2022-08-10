from django.shortcuts import render

def ana(request):
    return render(request, 'deneme/ana.html',{"dakka":41})