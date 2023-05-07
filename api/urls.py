from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import *


schema_view = get_swagger_view(title='Jokes Api')

urlpatterns = [
    path('jokes/external_jokes/',joke_external),
    path('jokes/create/',JokeCreate.as_view()),
    path('jokes/all_jokes/',JokeList.as_view()),
    path('jokes/<str:id>',JokeDetail.as_view()),
    path('jokes/delete/<str:id>',JokeDelete.as_view()),

]