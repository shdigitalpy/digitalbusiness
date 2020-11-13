from django.shortcuts import render
from datetime import datetime


def index(request):
	x = datetime.now()
	today = x.strftime('%m' + '.' + '%Y')
	now = x.strftime('%d' + '.' + '%m' + '.' + '%Y' + ' ' + '%H' + ':' + '%M')

	import random
	zufall = random.randint(5, 19)

	context = {'today': today, 'zufall': zufall, 'now': now }
	return render(request, 'index.html', context)
