from django.shortcuts import render
from .forms import BlogForm
from .models import BlogEntries
# Create your views here.

def blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        form.save()
    if request.method == 'GET':
        form = BlogForm()
    context = BlogEntries.objects.all()
    return render(request, 'home/blog.html', {'form': form,'context':context})
