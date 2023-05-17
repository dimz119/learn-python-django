from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "inventory/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Joon"
        return context