from django.shortcuts import render

# This is my views.py file
def home(request):
    return render(request, 'Index.html', {})    