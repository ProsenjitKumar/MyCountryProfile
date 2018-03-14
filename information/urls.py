from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^districts/', views.DistrictList, name='districts'),
    url(r'^divisions/', views.DivisionList, name='divisions'),
    #url(r'^dists-divs/(?P<divs_id>[0-9]+)/', views.DistsOfDivs, name='dists-divs'),
    url(r'^dists-divs/', views.DistsOfDivs, name='dists-divs'),
]