from django.urls import path, include
from . import views

urlpatterns = [
    #ここで指定するとdjango指定のurls.pyに進む
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
]

