# filepath: [urls.py](http://_vscodecontentref_/2)
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import render
from api.resources import NoteResource
from api.models import Note

note_resource = NoteResource()

def home(request):
    note_count = Note.objects.count()
    return render(request, "home.html", {"note_count": note_count})

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(note_resource.urls)),
    path('', include('api.urls')),
]