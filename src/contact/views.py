from django.shortcuts import render

# Create your views here.

def home(request):
    
    context = {}
    return render(request, 'contact/contact_page.html', context)
