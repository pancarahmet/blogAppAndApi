from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormMixin
from .forms import *

# Create your views here.
def index(request):
    return render(request,"index.html")

class PostListView(ListView):
    model=Post
    template_name="post-list.html"
    context_object_name='posts'

# def postDetay(request,pk):
#     post=Post.objects.get(id=pk)

class PostDetailView(FormMixin,DetailView):
    model=Post
    template_name="post-detail.html"
    context_object_name='post'
    form_class=CommentForm

    def get_success_url(self):
        return reverse('postDetay',kwargs={'pk':self.get_object().pk})
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        if 'comment_form' not in context:
            context['comment_form']=self.form_class()
        
        # ilgili postun yorumlarını getiriyor
        context['comments']=self.object.comments.all().order_by('-created_at')
        return context
    def post(self,request,*args,**kwargs):
        self.object=self.get_object() # detayı gördüğümüz postu alıyoruz
        form = self.get_form()        # form_class = CommentForm

        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.blog=self.object
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)



# class PostCreateView(CreateView):
#     model=Post
#     template_name="post-create.html"
#     fields=['title','content','author']
#     success_url= reverse_lazy('postList')


class PostCreateView(CreateView):
    model=Post
    template_name="post-create.html"
    fields=['title','content','resim']
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

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('postList')

    
    def dispatch(self, request, *args, **kwargs):
        post=self.get_object()
        if not (request.user==post.author or request.user.is_superuser):
            return HttpResponseForbidden("Bu postu silmeye yetkin yok")
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)




