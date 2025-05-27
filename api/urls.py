from django.urls import path
from .views import (
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView, NoteDetailView,
    export_notes_csv
)

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/add/', NoteCreateView.as_view(), name='note-add'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-edit'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('notes/export/csv/', export_notes_csv, name='export-notes-csv'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]