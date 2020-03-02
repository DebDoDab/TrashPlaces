from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from server import views
from rest_framework.urlpatterns import format_suffix_patterns
import djoser

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'campuses', views.CampusViewSet)
router.register(r'trashplaces', views.TrashPlacesViewSet)
router.register(r'trashstats', views.TrashStatsViewSet)
router.register(r'permissions', views.OwnPermissionViewSet)
router.register(r'campusstats', views.CampusStatsViewSet)

urlpatterns = [
    path('', include('server.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('djoser.urls.authtoken')),
]