from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('register/', v.register, name='register'),
    path('Edit/', v.Doc, name='Doc'),
]