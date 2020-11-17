from django.shortcuts import render, redirect
from datetime import datetime
from .models import Sender
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):

	if request.method == "POST" and 'button1' in request.POST:
		message_name = request.POST['name']
		message_vorname = request.POST['vorname']
		message_email = request.POST['email']
		message_telefon = request.POST['phone']
		message_category = 'E-Mail-Lead'
		
		send_mail(
			'FFHS - ' + message_category + ' ' + message_vorname + ' ' + message_name,
			message_category + ' '+ message_name + ' ' + message_vorname + ' E-Mail: ' + message_email + ' Telefon: ' + message_telefon,
			message_email,
			['sandro@sh-digital.ch'],
    		fail_silently=False,		
			)

		emailsender = Sender(message_name=message_name, message_vorname=message_vorname, message_email=message_email, message_telefon=message_telefon, message_category=message_category)
		emailsender.save()

		context = { 'message_vorname': message_vorname }
		return render(request, 'index.html', context)

	if request.method == "POST" and 'button2' in request.POST:
		message_name = request.POST['name']
		message_vorname = request.POST['vorname']
		message_email = request.POST['email']
		message_telefon = request.POST['phone']
		message_bemerkungen = request.POST['bemerkungen']
		message_category = 'Anmeldung FFHS Forward'

		send_mail(
			'FFHS - ' + message_category + ' ' + message_vorname + ' ' + message_name,
			message_category + ' '+ message_name + ' ' + message_vorname + ' E-Mail: ' + message_email + ' Telefon: ' + message_telefon + ' Bemerkungen: ' + message_bemerkungen,
			message_email,
			['sandro@sh-digital.ch'],
    		fail_silently=False,		
			)

		emailsender = Sender(message_name=message_name, message_vorname=message_vorname, message_email=message_email, message_telefon=message_telefon, message_bemerkungen=message_bemerkungen, message_category=message_category)
		emailsender.save()

		return redirect('https://registration.ffhs.ch/campus/campus/Portal/SelectApplicationProcedure?l=de&t=')
	else:

		x = datetime.now()
		today = x.strftime('%m' + '.' + '%Y')
		now = x.strftime('%d' + '.' + '%m' + '.' + '%Y' + ' ' + '%H' + ':' + '%M')

		import random
		zufall = random.randint(5, 19)

		context = {'today': today, 'zufall': zufall, 'now': now}
		return render(request, 'index.html', context)
