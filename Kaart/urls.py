from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/data$', views.get_kohad, name='api-data'),
    url(r'^api/kohad$', views.add_koht, name='kohad'),
]