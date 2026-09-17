from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Note, Task, Product
from rest_framework.generics import ListCreateAPIView
from .serializers import NoteSerializer


# def note_list(request):
#     if request.method != "GET":
#         return JsonResponse({"detail": "Method not allowed"}, status=405)

#     notes = list(Note.objects.values("id", "title", "text"))
#     return JsonResponse({"items": notes})

# def note_detail(request, pk):
#     if request.method != "GET":
#         return JsonResponse({"detail": "Method not allowed"}, status=405)

#     note = Note.objects.filter(pk=pk).values("id", "title", "text")
#     if not note:
#         return JsonResponse({"detail": "не найдено"}, status=404)

def product(request):
    if request.method != "GET":
        return JsonResponse({"detail": "Method not allowed"}, status=405)

    product = list(Product.objects.values("id", "name", "description", "price"))

    return JsonResponse({"items": product})


from rest_framework.test import APIClient

from notes.models import Note


def test_get_notes():
    client = APIClient()

    Note.objects.create(
        title="Первая заметка",
        text="Текст"
    )

    response = client.get("/api/notes/")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["title"] == "Первая заметка"


def test_create_note():
    client = APIClient()

    response = client.post(
        "/api/notes/",
        {
            "title": "Новая заметка",
            "text": "Описание"
        },
        format="json"
    )

    assert response.status_code == 201
    assert Note.objects.count() == 1
    assert response.data["title"] == "Новая заметка"

class NoteListView(ListCreateAPIView):    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer