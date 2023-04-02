from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from .serializers import *

import requests

# Create your views here.

def jokes(request):
    #pull data from third party rest api
    response = requests.get('https://joke.deno.dev/all')
    #convert reponse data into json
    jokes = response.json()
    print(jokes)
    return HttpResponse("jokes")
    pass


@csrf_exempt
def joke_endpoint(request):
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

        
