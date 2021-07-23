from django.urls import path
from .views import HomeView, ArticleDetatilView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetatilView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit-post'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category')
]
