from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from .models import Women, Category
from .serializers import WomenSrializer


# Create your views here.
class WomenPagination(PageNumberPagination):    #Pagination
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000



class WomenViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    #queryset = Women.objects.all()
    serializer_class = WomenSrializer
    permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    pagination_class = WomenPagination




    def get_queryset(self):                         #переопределяем queryset
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()#[:3](количество)              #urls --- basename='women'
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)          #добавляем маршрут категории
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})


    @action(methods=['get'], detail=True)           #маршут по конкретной категории
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})