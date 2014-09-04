from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect


# helper functions
def encode_url(url):
    return url.replace(' ','_')

def retrieve_posts(post_title = ''):
    if post_title != '':
        posts = get_object_or_404(Post, title = post_title.replace('_',' '))
        # posts = Post.objects.filter(title=post_title)
    else:
        posts = Post.objects.all().order_by('-created_at')
        for post in posts:
            post.url = encode_url(post.title)
    return posts

def pop_posts(n):
    pop_posts = Post.objects.order_by('-views')[:n]
    for post in pop_posts:
        post.url = encode_url(post.title)
    return pop_posts

# views
def index(request):
    t = loader.get_template('blog/index.html')
    context_dict = {'latest_posts': retrieve_posts(), 'popular_posts': pop_posts(5),}
    c = Context(context_dict)
    return HttpResponse(t.render(c))

# Create your views here.
def post(request, post_name):
    t = loader.get_template('blog/post.html')
    context_dict = {'single_post': retrieve_posts(post_name),'popular_posts': pop_posts(5),}
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): # is the form valid?
            form.save(commit = True) # yes? save to database
            # print request.POST.items()
            post_title = request.POST['title']
            return HttpResponse(post(request,post_title))
        else:
            print form.errors # no? Display errors to end user
    else:
        form = PostForm()
    return render_to_response('blog/add_post.html', { 'form': form}, context)
