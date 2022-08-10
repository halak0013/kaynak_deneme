from django.shortcuts import render

def hesaplama(request):
    return render(request, 'hesap.html')