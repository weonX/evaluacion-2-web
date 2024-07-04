from django.urls import path
from .views import Pagina1, Pagina2, Pagina3, Pagina4, Pagina5, Pagina6

urlpatterns = [
    path('', Pagina1, name= 'Pagina1'),
    path('Pagina2/', Pagina2, name= 'Pagina2'),
    path('Pagina3/', Pagina2, name= 'Pagina3'),
    path('Pagina4/', Pagina2, name= 'Pagina4'),
    path('Pagina5/', Pagina2, name= 'Pagina5'),
    path('Pagina6/', Pagina2, name= 'Pagina6'),
]