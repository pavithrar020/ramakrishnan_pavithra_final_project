from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

urlpatterns = [

    path('',
         RedirectView.as_view(
             pattern_name='about_urlpattern',
             permanent=False
         )),

    path('about/',
         TemplateView.as_view(
             template_name='cities/about.html'),
         name='about_urlpattern'
         ),

    path('login/',
         LoginView.as_view(template_name='cities/login.html'),
         name='login_urlpattern'
         ),

    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'
         ),

    path('admin/', admin.site.urls),

    path('', include('cities.urls'))
]

# Include static and media URL patterns during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
