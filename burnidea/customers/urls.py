from django.urls import path, include
from .views import RegisterView, LoginView, CustomerDetailView, CustomerUpdateView, AdminDetailView, AdminAuthView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', CustomerDetailView.as_view(), name='customer-detail'),
    path('update/', CustomerUpdateView.as_view(), name='customer-update'),
    path('me/admin/', AdminAuthView.as_view(), name='admin-auth'),
    path('admin/', AdminDetailView.as_view(), name='admin-detail'),
]