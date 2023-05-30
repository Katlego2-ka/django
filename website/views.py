
# Create your views here.
from django.shortcuts import render

def detail(request):
    return render(request, 'about_candidate.html',)

def results(request):
    return render(request, 'contacts.html', )

def vote(request):
    return render(request, 'goal.html',)