# cookie_stands/urls.py

from django.urls import path
from .views import CookieStandList, CookieStandDetail

urlpatterns = [
  path("", CookieStandList.as_view(), name="cookie_stands_list"),
  path("<int:pk>/", CookieStandDetail.as_view(), name="cookie_stands_detail"),
]
