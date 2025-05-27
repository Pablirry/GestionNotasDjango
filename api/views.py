from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Note
from .forms import NoteForm
from django.contrib import messages
import csv
from django.http import HttpResponse

def export_notes_csv(request):
    notes = Note.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="notas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Título', 'Contenido', 'Favorita', 'Creada'])
    for note in notes:
        writer.writerow([note.title, note.body, note.favorite, note.created_at])
    return response

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        q = self.request.GET.get('q')
        order = self.request.GET.get('order')
        if q:
            queryset = queryset.filter(title__icontains=q) | queryset.filter(body__icontains=q)
        if order == 'favorite':
            queryset = queryset.order_by('-favorite', '-created_at')
        return queryset

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        messages.success(self.request, "Note created successfully.")
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        messages.success(self.request, "Note updated successfully.")
        return super().form_valid(form)

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_confirm_delete.html'
    success_url = reverse_lazy('note-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Note deleted successfully.")
        return super().delete(request, *args, **kwargs)

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'