from django.apps import AppConfig


class NotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'

    def ready(self):
        # Закомментируйте эту строку, так как файла signals.py пока нет:
        # import notes.signals
        pass