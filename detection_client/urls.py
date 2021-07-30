from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'histo', views.HistoriqueViewSet)
router.register(r'photo', views.PhotoViewSet)

urlpatterns = [
    path('clients', views.clients, name='clients'),
    path('client_detail', views.client_detail, name='cli_detail'),
    path('photos', views.photos, name='photos'),
    path('new_photo', views.new_photo, name='new_photo'),
    path('det_photo', views.det_photo, name='det_photo'),
    path('edithisto/<int:id>/', views.histo_edit, name='histo_edit'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls',namespace='rest_framework_detect'), name='api')
    ]


