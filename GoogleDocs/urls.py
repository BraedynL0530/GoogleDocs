from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('register/', v.register, name='register'),
    path('edit/<uuid:doc_id>/', v.edit_document, name='edit_document'),
    path('update-title/<uuid:doc_id>/', v.update_title, name='update_title'),
    path('create/', v.create_document, name='create_document'),
    path('update-content/<uuid:doc_id>/', v.update_content, name='update_content'),
    path('share/<uuid:doc_id>/', v.share_document, name='share_document'),
    path('check-template/', check_template),

]