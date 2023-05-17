from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = "inventory/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Joon"
        return context
    
from django.views.generic.edit import FormView
from inventory.forms import CarForm
from django.urls import reverse_lazy, reverse

class CarFormView(FormView):
    template_name = 'inventory/car_basic_form.html'
    form_class = CarForm
    # success_url = '/inventory'

    # # why can't we use reverse?
    # # because then reverse is called when the module is imported, before the urls have been loaded.
    # # class attributes are evaluated on import,
    # # success_url = reverse("inventory:main")
    # # Reverse_lazy is, as the name implies, a lazy implementation of the reverse URL resolver. Unlike the traditional reverse function, reverse_lazy won't execute until the value is needed.
    # # It is useful because it prevent Reverse Not Found exceptions when working with URLs that may not be immediately known.
    # # finally, reverse returns the str vs. reverse_lazy returns the object
    success_url = reverse_lazy("inventory:main")
    

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.do_action()
        print(form.cleaned_data)
        return super().form_valid(form)
