from django.urls import path, include
from django.contrib import admin
from django.http import HttpResponse
from api.resources import NoteResource

note_resource = NoteResource()

def home(request):
    html = """
    <html>
        <head>
            <title>Notable Django API</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@1.0.0/css/bulma.min.css">
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; }
                .container { background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px #eee; }
                h1 { color: #2c3e50; }
                ul { margin-top: 20px; }
                a { color: #2980b9; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="title">Welcome to Notable Django</h1>
                <p>This is a RESTful API and web app for managing notes.</p>
                <h2 class="subtitle">Available endpoints:</h2>
                <ul>
                    <li><a href="/admin/">/admin/</a> – Django Admin</li>
                    <li><a href="/api/note/">/api/note/</a> – Notes API (GET, POST, etc.)</li>
                    <li><a href="/notes/">/notes/</a> – Web Notes App</li>
                </ul>
                <h2 class="subtitle">API Example</h2>
                <pre>
GET /api/note/
POST /api/note/ {"title": "...", "body": "..."}
                </pre>
                <p>See <a href="https://django-tastypie.readthedocs.io/en/latest/">Tastypie docs</a> for more info.</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(note_resource.urls)),
    path('', include('api.urls')),
]