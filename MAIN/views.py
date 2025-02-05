from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def forum(request):
    return render(request,'forum.html')

def policy(request):
    return render(request,'policy.html')
