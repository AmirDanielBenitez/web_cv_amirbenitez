from django.urls import path
from . import views

urlpatterns = [
    path("", views.PorfolioPage.as_view(), name="portfolio-page"),
]