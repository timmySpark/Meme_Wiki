from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

import requests

# Create your views here.

# Get Jokes from External Api

@csrf_exempt
def joke_external(request):
    # Make a GET request to the external API endpoint
    response = requests.get('https://joke.deno.dev/all')

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the data from the API response
        data = response.json()

        # Create instances of the ExternalData model using the retrieved data
        for item in data:
            external_data = Joke(
                id = item['id'],
                type=item['type'],
                setup=item['setup'],
                punchline=item['punchline']
            )
            external_data.save()

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})
    else:
        # Return a JSON response indicating failure
        return JsonResponse({'status': 'failure'})


# Get all Jokes in Database 
class JokeList(generics.ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['type']
    ordering_fields = ['type','setup']


#  Get a Joke from the Database
class JokeDetail(generics.RetrieveAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    lookup_field=('id')


#  Create a Joke
class JokeCreate(generics.CreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#  Delete a Joke
class JokeDelete(generics.DestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    lookup_field = ('id')



'''
To be back 

@api_view(['GET'])
def jokes_list(request):
    if request.method == 'GET':
        jokes = Joke.objects.all()
        serializer = JokeSerializer(jokes,many=True)
        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def jokes_details(request,id):
    try:
        joke = Joke.objects.get(pk=id)
    except Joke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = JokeSerializer(joke)
        return Response(serializer.data)
    elif request.method == 'PUT' :
        serializer = JokeSerializer(joke,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        joke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
