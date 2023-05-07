from rest_framework import serializers
from .models import *


class JokeSerializer(serializers.ModelSerializer):
    class Meta :
        model = Joke
        fields = "__all__"
