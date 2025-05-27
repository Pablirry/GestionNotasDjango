from .models import Note

def note_count(request):
    return {'note_count': Note.objects.count()}