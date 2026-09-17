# import pytest
# from django.urls import reverse

# from .models import Note


# @pytest.mark.django_db
# def test_note_is_saved():
#     note = Note.objects.create(title="First note", text="Hello")

#     assert note.title == "First note"
#     assert Note.objects.count() == 1


# @pytest.mark.django_db
# def test_note_list_returns_notes(client):
#     Note.objects.create(title="First note", text="Hello")

#     response = client.get(reverse("note-list"))

#     assert response.status_code == 200
#     assert response.json() == {
#         "items": [
#             {"id": 1, "title": "First note", "text": "Hello"},
#         ]
#     }


# def test_note_list_rejects_post(client):
#     response = client.post(reverse("note-list"))

#     assert response.status_code == 405