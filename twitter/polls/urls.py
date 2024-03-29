from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("results/<int:question_id>", views.results, name="results"),
    # ex: /polls/5/vote/
    path("vote/<int:question_id>", views.vote, name="vote"),
]