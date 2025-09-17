import os
from django.conf import settings
from django.core.management import call_command
from django.db.utils import OperationalError

def cleanup_on_start():
	# Видалити всі фото з media/places/
	media_places = os.path.join(settings.MEDIA_ROOT, 'places')
	if os.path.exists(media_places):
		for f in os.listdir(media_places):
			try:
				os.remove(os.path.join(media_places, f))
			except Exception:
				pass
	# Видалити всі місця з бази
	try:
		from places.models import Place
		Place.objects.all().delete()
	except OperationalError:
		pass

def ready():
	cleanup_on_start()

try:
	cleanup_on_start()
except Exception:
	pass
