from django.conf.urls import url
from .views import import HomeView

urlpatterns =[
    url(r'^$', HomeView.as_view(), name='home'),
]
