from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def mitgliedwerden(request):
    return render(request, 'main/mitgliedwerden.html')

def preise(request):
    return render(request, 'main/preise.html')

def kontakt(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        betreff = request.POST['betreff']
        nachricht = request.POST['nachricht']

        ganze_nachtricht = "E-Mail: " + email + "\r\r\nName: " + name + "\r\r\nNachricht:" + "\r\n" + nachricht

        send_mail(
            betreff,
            ganze_nachtricht,
            settings.EMAIL_HOST_USER,
            ['boxfit.mainspessart@gmail.com'],
            fail_silently=True)

        return redirect('kontakterfolgreich')

    return render(request, 'main/kontakt.html')

def kontakterfolgreich(request):
    return render(request, 'main/kontakterfolgreich.html')


def impressum(request):
    return render(request, 'main/impressum.html')


def datenschutz(request):
    return render(request, 'main/datenschutz.html')