from django.apps import AppConfig


class NotesappConfig(AppConfig):
    name = 'notesapp'

    def ready(self):
        import notesapp.signals


