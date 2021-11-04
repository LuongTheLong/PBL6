from django.conf.urls import url
from Recommend_Web.account import views


urlpatterns = [
    url(r'get_accounts$', views.getAccounts),
    url(r'create_account$', views.createAccount),
    url(r'update_account$', views.updateAccount),
    url(r'delete_account$', views.deleteAccount),
    url(r'login_account$', views.loginAccount),
    url(r'logout_account$', views.logoutAccount),
    url(r'check_token$', views.checkToken)
]
