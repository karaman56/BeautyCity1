from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def service_finally(request):
    return render(request, 'serviceFinally.html')

def notes(request):
    return render(request, 'notes.html')

def admin_panel(request):
    return render(request, 'admin.html')