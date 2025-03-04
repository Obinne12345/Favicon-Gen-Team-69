import imp
from django.urls import path
from favicon import views

urlpatterns = [
    path('favicons/', views.FaviconListView.as_view(), name='favicon_list'),
    path('favicon_update/<int:pk>/', views.UpdateFaviconView.as_view(), name='favicon_update'),
    path('favicon_generate/', views.CreateFaviconView.as_view(), name='favicon_generate'),
    path('text_preview/', views.TextFaviPreview.as_view(), name='text_preview'),
    path('emoji_preview/', views.EmojiFaviPreview.as_view(), name='emoji_preview'),

]