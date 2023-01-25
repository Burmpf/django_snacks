from django.urls import path

from .views import AboutView, HomePageView, SnackListView, SnackDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("snacks/", SnackListView.as_view(), name="snack_list"),
    path("snacks/<int:pk>/", SnackDetailView.as_view(), name="snack_detail"),
]

