from django.shortcuts import render

# Create your views here.

from .models import Post, User, Feed, Topic
from .forms import PostForm

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

def get_post(posting, pk):
    #postInst=get_object_or_404(post_inst, pk = pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            postInst.post = form.cleaned_data['text']
            postInst.save()

            return HTTPResponseRedirect(reverse('/'))

            #postInst.post = form.cleaned_data['post_date']
            #postInst.save()
            return HTTPResponseRedirect(reverse('/archive/'))


    return render(
        request,
        'posting.html',
        {'form': form}
    )

def login(request):
    return render(
        request,
        'login.html',
    )

def profile(request):
    return render(
        request,
        'profile.html'
    )

def about(request):
    return render(
        request,
        'about.html'
    )

def posting(request):
    return render(
        request,
        'posting.html'
    )

from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 20

class PostDetailView(generic.DetailView):
    model = Post


from django.contrib.auth.mixins import LoginRequiredMixin

class PostsByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing posts made by current user. 
    """
    model = Post
    template_name ='catalog/posts_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(poster=self.request.poster).filter(status__exact='o')#.order_by('date_posted')





