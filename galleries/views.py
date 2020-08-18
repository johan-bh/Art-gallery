from django.shortcuts import render
from galleries.models import AboutText, ContactText, UploadImage
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from galleries.forms import ContactForm


def index(request):
	"""Returns the index page"""
	about_text = AboutText.objects.get()
	contact_text = ContactText.objects.get()
	images = UploadImage.objects.all()


	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)

	if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = ['********']
	    message = "FROM: " + sender + "\n\nMESSAGE:" + "\n\n" + message
	    send_mail(subject, message, sender, recipients, fail_silently=False)

	    return HttpResponseRedirect("/")
 

	else:
		return render(request, 'galleries/index.html', {'about_text': about_text,'contact_text': contact_text,'images': images})







