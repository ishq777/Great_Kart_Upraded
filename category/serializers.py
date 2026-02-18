from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['cat_image']
        #fields = "__all__"
