from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions

from .models import Women, Category
from .serializers import WomenSrializer


# Create your views here.
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




    def get_queryset(self):                         #переопределяем queryset
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]              #urls --- basename='women'
        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)          #добавляем маршрут категории
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})


    @action(methods=['get'], detail=True)           #маршут по конкретной категории
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})