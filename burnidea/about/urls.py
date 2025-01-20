from django.urls import path, include
from .views import AboutListCreateView, AboutDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', AboutListCreateView.as_view(), name='About-list-create'),
    path('<int:pk>/', AboutDetailView.as_view(), name='About-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)