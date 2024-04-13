from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples =[
        {'name':'Twinkle Gulhane','age':24},
        {'name':'Kanchan Gulhane','age':26},
        {'name':'Vedant Gulhane','age':19},
        {'name':'Mansvi Gulhane','age':12},
        {'name':'Piya Gulhane','age':15}
    ]

    vegetables =['Potato','Tomato','Bhendi']

    return render(request, "index.html" , context = {'page':'Django Learning','peoples':peoples,'vegetables':vegetables})

def about(request):
    context = {'page':'About'}
    return render(request, "about.html",context)

def contact(request):
    context = {'page':'Contact'}
    return render(request, "contact.html",context)  

