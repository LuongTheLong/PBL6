from django.conf.urls import url
from Recommend_Web.location import views


urlpatterns = [
    url(r'get_locations$', views.getLocations),
    # url(r'importcounts$', views.importCounts),
    url(r'create_location$', views.createLocation),
    # url(r'deleteaccount$', views.deleteAccount),
    # url(r'loginaccount$', views.loginAccount)
    url(r'map_reduce$', views.mapReduce)
]