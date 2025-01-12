from django.urls import path, include
from .views import FAQListCreateView, FAQDetailView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', FAQListCreateView.as_view(), name='FAQ-list-create'),
    path('<int:pk>/', FAQDetailView.as_view(), name='FAQ-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)