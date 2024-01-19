from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form=ContactForm()

    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # enviamos el correo y redireccionamos
            email=EmailMessage(
                "La Caggettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["encinah030@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # funciona, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #algo a salido mal, redireccionamos a fail
                return redirect(redirect('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
