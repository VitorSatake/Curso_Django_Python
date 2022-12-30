
from django.urls import path
from recipes.views import home, contato, sobre

# HTTP REQUEST <- HTTP RESPONSE
#HTTP Request
# return HTTP Response

urlpatterns = [
    path('', home), # HOME
    path('sobre/', sobre), # /sobre/
    path('contato/', contato), # /contato/
]
