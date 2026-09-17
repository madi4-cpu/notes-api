from rest_framework.test import APIClient
from rest_framework import status
from notes.models import Note
import pytest


@pytest.mark.django_db
def test_get_notes():
    client = APIClient()
    Note.objects.create(title="Первая заметка", text="Текст")
    
    response = client.get("/api/notes/")
    
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["title"] == "Первая заметка"


@pytest.mark.django_db
def test_create_note():
    client = APIClient()
    payload = {
        "title": "Новая заметка",
        "text": "Описание"
    }
    
    response = client.post("/api/notes/", data=payload, format="json")
    
    # Проверки (Assertions)
    assert response.status_code == status.HTTP_201_CREATED
    assert Note.objects.count() == 1
    assert response.data["title"] == "Новая заметка"