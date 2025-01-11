from django.urls import path, include
from .views import IdeaListCreateView, IdeaDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', IdeaListCreateView.as_view(), name='idea-list-create'),
    path('<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)