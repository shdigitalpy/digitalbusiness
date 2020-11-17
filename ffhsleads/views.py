from django.shortcuts import render
from datetime import datetime
from .models import Sender
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):

	if request.method == "POST":
		message_name = request.POST['name']
		message_vorname = request.POST['vorname']
		message_email = request.POST['email']
		message_telefon = request.POST['phone']
		message_bemerkungen = request.POST['bemerkungen']

		send_mail(
			'FFHS Anfrage - ' + message_name + message_vorname,
			'Name: '+ message_name + ' Vorname: ' + message_vorname + ' E-Mail: ' + message_email + ' Telefon: ' + message_telefon + ' Bemerkungen: ' + message_bemerkungen,
			message_email,
			['sandro@sh-digital.ch'],
    		fail_silently=False,		
			)
		success_message = 'Die Nachricht wurde gesendet!'
		return render(request, 'index.html', {'message_vorname': message_vorname})
	else:

		x = datetime.now()
		today = x.strftime('%m' + '.' + '%Y')
		now = x.strftime('%d' + '.' + '%m' + '.' + '%Y' + ' ' + '%H' + ':' + '%M')

		import random
		zufall = random.randint(5, 19)

		context = {'today': today, 'zufall': zufall, 'now': now}
		return render(request, 'index.html', context)
