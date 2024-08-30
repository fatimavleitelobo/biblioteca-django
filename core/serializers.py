from rest_framework import serializers
from .models import Categoria, Autor, Livro

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    categoria = CategoriaSerializer()
    class Meta:
        model = Livro
        fields = '__all__'