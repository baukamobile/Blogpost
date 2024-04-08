from django.shortcuts import render, HttpResponse, reverse, get_object_or_404, redirect
from .models import Blog, Author
from .forms import BlogForm
# Create your views here.


def showPost(request):
    blog = Blog.objects.all()
    form = BlogForm()
    return render(
        request,
        'main.html',
    context={
        'blog':blog,
        'form': form,
    }
    )

def createBlog(request):
    blog = Blog.objects.all()
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showpost')
        else:
            print(form.errors)
    return render(request, 'main.html', context={
         'task': blog,
         'form': form,
        })

def deleteBlog(request, pk):
    delBlog = Blog.objects.get(id=pk)
    delBlog.delete()
    return redirect('showpost')

def updateBlog(request, pk):
    update = Blog.objects.get(id=pk)
    form = BlogForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        return redirect('showpost')
    form = BlogForm(instance=update)
    return render(request, 'update.html', context={
        'update':update,
        'form': form
    })
