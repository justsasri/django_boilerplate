import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse


class LogoutView(BaseLogoutView):
    template_name = "app/logout.html"


class LoginView(BaseLoginView):
    template_name = "app/login.html"
    extra_context = {
        "title": "Please login to start",
    }

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("dashboard-index")

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            # coba login, kalau gagal panggil exception
            error_message = {"errors": "Maaf username dan password gak matching!"}
            data = json.loads(request.body.decode("utf-8"))
            form = AuthenticationForm(request, data)
            if form.is_valid():
                cleaned_data = form.clean()
                user = authenticate(request, **cleaned_data)
                if user:
                    login(request, user)
                    return JsonResponse(
                        {
                            "message": "Login succesfully",
                            "redirect_url": self.get_success_url(),
                        },
                    )
                else:
                    return JsonResponse(error_message, status=201)
            else:
                return JsonResponse(error_message, status=201)
        else:
            return super().post(request, *args, **kwargs)
