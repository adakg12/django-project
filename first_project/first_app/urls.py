
from django.urls import path
from first_app import views
from django.conf.urls import include

app_name = 'first_app'

urlpatterns = [
    path('help/',views.help,name='help'),
    path('register/',views.register,name='register'),
    # path('users/',views.user_display,name='users'),
    
]