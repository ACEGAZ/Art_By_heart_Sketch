"""imports from urls and views"""
from django.urls import path
from . import views
from .views import AddCommentView, UpdateCommentView, DeleteCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.display_artwork, name='gallery'),
    path('commissions/', views.commission_view, name='commissions'),
    path('admin_upload_art/', views.upload_art_view, name='admin_upload_art'),
    path('add_comment_success', views.add_comment_success,
         name='add_comment_success'),
    path('add_comment/<int:pk>/', AddCommentView.as_view(),
         name='add_comment'),
    path('add_comment_success/', views.add_comment_success,
         name='add_comment_success'),
    path('update_comment/<int:pk>/', UpdateCommentView.as_view(),
         name='update_comment'),
    path('delete_comment/<int:pk>/', DeleteCommentView.as_view(),
         name='delete_comment'),
]
