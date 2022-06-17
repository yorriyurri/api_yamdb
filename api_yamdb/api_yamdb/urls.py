from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path

from api.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns), name='api'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
