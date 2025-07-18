from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post, Category, Tag

class PostListView(ListView):
    """
    Class-based view for listing posts
    Advantages: Less code, built-in pagination, standard patterns
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.filter(status='published')[:3]
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    """
    Class-based view for post details
    """
    model = Post
    template_name = 'blog/post_detail_cbv.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = post.comments.filter(is_approved=True)
        context['related_posts'] = Post.objects.filter(
            category=post.category,
            status='published'
        ).exclude(id=post.id)[:3]
        return context

        
def home(request):
    """
    Home page view - displays latest published posts
    """
    # Get published posts ordered by creation date
    posts = Post.objects.filter(status='published').order_by('-created_at')
    
    # Add pagination (5 posts per page)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get recent posts for sidebar
    recent_posts = Post.objects.filter(status='published')[:3]
    
    # Get all categories for sidebar
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, slug):
    """
    Individual post detail view
    """
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Get approved comments for this post
    comments = post.comments.filter(is_approved=True).order_by('created_at')
    
    # Get related posts (same category, excluding current post)
    related_posts = Post.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_posts(request, slug):
    """
    View posts by category
    """
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    
    # Add pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'blog/category_posts.html', context)

def tag_posts(request, slug):
    """
    View posts by tag
    """
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, status='published')
    
    # Add pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'tag': tag,
        'page_obj': page_obj,
    }
    return render(request, 'blog/tag_posts.html', context)