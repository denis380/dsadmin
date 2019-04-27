from django.contrib import admin
from django.urls import path, include
from impressora import urls as impressora_urls
from django.contrib.auth import views as auth_viws
from impressora.views import inicio



urlpatterns = [
    path('printers/', include(impressora_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_viws.LoginView.as_view(), name='login'),
    path('logout/', auth_viws.LogoutView.as_view(), name='logout'),
    path('', inicio, name='inicio'),
]
