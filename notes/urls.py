from django.urls import path

from .views import product,  NoteListView


urlpatterns = [
    path("product/", product, name="product-list"),
    path("notes/", NoteListView.as_view()),
]