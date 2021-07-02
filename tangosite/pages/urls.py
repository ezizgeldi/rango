from django.urls import path
from .views import HomePageView,  AboutPageView

app_name = 'pages'


urlpatterns = [
    # path('', views.index, name='index'),
    path('', HomePageView.as_view(), name=('homepage')),
    path('about/', AboutPageView.as_view(), name=('about'))
]   
