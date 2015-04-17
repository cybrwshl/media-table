import logging

from django.http import HttpResponse
from django.template import RequestContext, loader
import webcolors

from mediatable_web.models import SimpleColor
from mediatable_web.forms import SimpleColorForm
from zmqcom import send_color_json


logger = logging.getLogger(__name__)


def index(request):
	if request.method == 'POST':
		form = SimpleColorForm(request.POST)
		if form.is_valid():
			new_color = SimpleColor()
			r = form.cleaned_data['red']
			g = form.cleaned_data['green']
			b = form.cleaned_data['blue']
			new_color.set_color_from_rgb((r, g, b))

			# first delete all existing entries
			# because we only want one entry at a time, which is the current color
			SimpleColor.objects.all().delete()

			# then save the new
			new_color.save()
		else:
			logger.debug(form.errors)

	current = get_current_or_create_default_color()
	red, green, blue = webcolors.hex_to_rgb(current.hex_color)

	# send a message via zmq
	send_color_json((red, green, blue))

	form = SimpleColorForm()
	context = RequestContext(request, {'current': current, 'red': red, 'green': green, 'blue': blue, 'form': form})

	template = loader.get_template('mediatable_web/index.html')
	return HttpResponse(template.render(context))


def get_current_or_create_default_color():
	results = SimpleColor.objects.order_by('-date_of_creation')[:1]

	if results:
		current = results[0]
	else:
		current = SimpleColor()
		current.set_default_color()
		current.save()

	return current
