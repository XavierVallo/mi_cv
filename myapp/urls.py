from django.urls import path
from .views import ContactView, home, skills, projects, about

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('contact/', ContactView.as_view(), name='contact'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'), # Página de proyectos
    path('about/', about, name='about'),
]
