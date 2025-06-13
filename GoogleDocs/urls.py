from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('register/', v.register, name='register'),
    path('edit/<uuid:doc_id>/', v.edit_document, name='edit_document'),
    path('update-title/<uuid:doc_id>/', v.update_title, name='update_title'),
    path('create/', v.create_document, name='create_document'),

]