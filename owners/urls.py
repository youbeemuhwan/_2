from django.urls import path
from owners.views import owner_signup_view, dog_signup_view

urlpatterns = [
    path('owners', owner_signup_view.as_view()),
    path('dogs', dog_signup_view.as_view()),
]
