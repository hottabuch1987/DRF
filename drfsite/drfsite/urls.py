
from django.contrib import admin
from django.urls import path, include

from women.views import WomenViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'women', WomenViewSet, basename='women')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
#    path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
#   path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]





#Кастомный Router
##Кастомный Router
#
# from django.contrib import admin
# from django.urls import path, include
#
# from women.views import WomenViewSet
#
# from rest_framework import routers
#
# #Кастомный Router
# class MyCastomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}/$',
#                      mapping={'get':'list'},
#                      name='{basename}-list',
#                      detail=False,
#                      initkwargs={'suffix':'list'}),
#         routers.Route(url=r'^{prefix}/{lookup}/$',
#                      mapping={'get':'retrieve'},
#                      name='{basename}-detail',
#                      detail=True,
#                      initkwargs={'suffix':'Detail'}),
#      ]
# #
# router = MyCastomRouter()
# router.register(r'women', WomenViewSet, basename='women')
#
# # router = routers.DefaultRouter()
# # router.register(r'women', WomenViewSet, basename='women')
# #
# #
# #
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),]