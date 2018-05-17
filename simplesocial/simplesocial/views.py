# Create views for the base.html file
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'

