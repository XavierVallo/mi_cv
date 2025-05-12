from django.shortcuts import render, redirect

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                subject=f'Mensaje de {form.cleaned_data["name"]}',
                message=form.cleaned_data['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect('contact')  # Redirige a la misma página con el mensaje
        return render(request, 'contact.html', {'form': form})
    
def home(request):
    return render(request, 'home.html')

def skills(request):
   return render(request, 'skills.html') 

def projects(request):
   return render(request, 'projects.html') 

def about(request):
   return render(request, 'about.html') 