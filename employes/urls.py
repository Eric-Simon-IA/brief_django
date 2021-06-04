from django.urls import path, include
from . import views
from rest_framework import routers

# Définition du router pour les deux modèles
# Cela permet le support automatique des routes (URLs) ppour l'API eu utilisant les viewset
# En incluant le router dans urlpatterns, cela me permet par exemple d'accéder à /employes/api/dept/ pour la
# liste des départements
router = routers.DefaultRouter()
router.register(r'dept', views.DepartementViewSet)
router.register(r'emp', views.EmployeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('dep_emp', views.dep_emp, name='dep_emp'),
    path('dep_list', views.dep_list, name='dep_list'),
    path('dep_detail', views.dep_detail, name='dep_detail'),
    path('dep_delete', views.dep_delete, name='dep_delete'),
    path('emp_delete', views.emp_delete, name='emp_delete'),
    path('dep_update_create', views.dep_update_create, name='dep_update_create'),

    path('api/', include('rest_framework.urls',namespace='rest_framework'), name='api'),
]
