from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home_view'),
    path('qrGenerator/', views.qrGenerator, name='qr_view'),
    path('apiEnd/', views.qrGenerator, name='api_end')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)