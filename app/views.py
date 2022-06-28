from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class AppView(TemplateView):
    template_name = "app/index.html"
    extra_context = {
        "title": "Welcome Home!",
    }


@method_decorator([login_required], name="dispatch")
class AdminView(TemplateView):
    template_name = "adm/index.html"
    extra_context = {
        "title": "Welcome to Your Dashboard!",
    }
