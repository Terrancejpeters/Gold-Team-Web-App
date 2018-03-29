from django.shortcuts import render

# Create your views here.

from .models import Post, User, Feed, Topic

def feed(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_posts=Post.objects.all().count()
    num_users=User.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template home.html with the data in the context variable
    return render(
        request,
        'feed.html',
        # context={'num_posts':num_posts},
    )

def login(request):
    return render(
        request,
        'login.html',
    )

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 20

class PostDetailView(generic.DetailView):
    model = Post
