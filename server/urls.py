""" server URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.http.response import JsonResponse
from django.urls import include, path  # NOQA

# from app.views import LandingPageView


def noexist(request):
    print(request.GET.get("code"))
    return JsonResponse(str(request.user.username), safe=False)


urlpatterns = [
    path("", include("app.urls")),
    path("api/", include("api.urls")),
    path("django-admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
