from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.upload_document, name='upload_document'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('delete/<int:document_id>/', views.delete_document, name='delete_document'),
    path('edit/<int:document_id>/', views.edit_description, name='edit_description'),
]

# Add this line to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
