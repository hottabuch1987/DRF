from rest_framework import serializers

from .models import Women


class WomenSrializer(serializers.ModelSerializer):
    class Meta():
        model = Women
        fields = ('title', 'cat_id')