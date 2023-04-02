from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from .views import *


schema_view = get_swagger_view(title='Jokes Api')

urlpatterns = [
    path('', jokes, name = 'jokes'),
    path('external_jokes/',joke_endpoint),
    path('all_jokes/',jokes_list),
    path('jokes/<str:id>',jokes_details)
]