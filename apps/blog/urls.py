from django.urls import path
from . import views

# This creates a namespace for our blog URLs
app_name = 'blog'

urlpatterns = [
    # Home page - Function-based view
    path('', views.home, name='home'),
    
    # Post detail - Function-based view
    # <slug:slug> captures a slug from URL and passes it to the view
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    # Category posts
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    
    # Tag posts
    path('tag/<slug:slug>/', views.tag_posts, name='tag_posts'),
    
    # Class-based views (alternative implementations)
    path('posts/', views.PostListView.as_view(), name='post_list_cbv'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_cbv'),
]