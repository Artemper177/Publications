from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from web.models import Publication

def index(request):
    return render(request, 'main.html')

def contacts(request):
    return render(request, 'contacts.html')

def post(request):
    request.method == 'POST:'
    title = request.POST.get('title')
    text = request.POST.get('text')
    if title and text:
        Publication.objects.create(title=title, text=text)
        return redirect('/publications')
    else:
        return render(request, 'post.html', {
            'error': 'title and text not found'
        })
    return render(request, 'post.html')

def publications(request):
    publications_sorted = Publication.objects.order_by('-date')
    return render(request, 'publications.html', {
        'publications': publications_sorted
    })

def publication(request, pub_id):
    try:
        publication = Publication.objects.get(id=pub_id)
    except Publication.DoesNotExist:
        return redirect('/')
    return render(request, 'publication.html', {
        'publication': publication
    })

def status(request):
    return HttpResponse("sdgsdgsd2323523")