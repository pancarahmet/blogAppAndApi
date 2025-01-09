from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

class PostListView(ListView):
    model=Post
    template_name="post-list.html"
    context_object_name='posts'

# def postDetay(request,pk):
#     post=Post.objects.get(id=pk)

class PostDetailView(DetailView):
    model=Post
    template_name="post-detail.html"
    context_object_name='post'

# class PostCreateView(CreateView):
#     model=Post
#     template_name="post-create.html"
#     fields=['title','content','author']
#     success_url= reverse_lazy('postList')


class PostCreateView(CreateView):
    model=Post
    template_name="post-create.html"
    fields=['title','content']
    # success_url=reverse_lazy('postList') # yöntem 1

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):   #yöntem 2
        return reverse_lazy('postList') 
class PostUpdateView(UpdateView):
    model=Post
    template_name="post-create.html"
    fields=['title','content']
    success_url=reverse_lazy('postList')

class PostDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('postList')

    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)
    

