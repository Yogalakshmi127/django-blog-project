from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, Aboutus
from .forms import ContactForm
from django.http import Http404
from django.core.paginator import Paginator
import logging

# Create your views here.
#posts = [
#    {'id':1,'title':'post1','content':'content of post 1'},
#    {'id':2,'title':'post2','content':'content of post 2'},
#    {'id':3,'title':'post3','content':'content of post 3'},
#    {'id':4,'title':'post4','content':'content of post 4'},
#]
def index(request):
    blog_title = "Latest Posts"
    all_posts = Post.objects.all()
    #paginate
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html",{'blog_title':blog_title,'page_obj': page_obj})
def detail(request, slug):
    #static data
    #post = next((item for item in posts if item['id'] == post_id),None)
    #getting dynamic data by id
    try:
        post = Post.objects.get(slug = slug)
        related_posts  = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exists!")
    #logger = logging.getLogger("TESTING")
    #logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html', {'post': post, 'related_posts':related_posts})
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger = logging.debug(f'POST DATA is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = 'your email has been sent'
            return render(request, 'blog/contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug("Form Validation failure")
        return render(request, 'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request, 'blog/contact.html')
def about_view(request):
    about_content = Aboutus.objects.first().content
    return render(request,'blog/about.html', {'about_content':about_content})
def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))
def new_url_view(request):
    return HttpResponse("this is the new url")

