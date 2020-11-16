from django.db import models

class Sender(models.Model):
	message_name = models.CharField(max_length=255)
	message_vorname = models.CharField(max_length=255, blank=True, null=True)
	message_email = models.CharField(max_length=255)
	message_telefon = models.IntegerField(blank=True, null=True)
	message_bemerkungen = models.CharField(max_length=1000, blank=True, null=True)

	def __str__(self):
		return str(self.pk) + self.message_name