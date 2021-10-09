from django.conf.urls import url
from Recommend_Web.location import views


urlpatterns = [
    url(r'getlocations$', views.getLocations),
    # url(r'importcounts$', views.importCounts),
    url(r'createlocation$', views.createLocation),
    # url(r'deleteaccount$', views.deleteAccount),
    # url(r'loginaccount$', views.loginAccount)
]