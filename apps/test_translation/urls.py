from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_language$', views.TestLanguageView.as_view(), name='test_language'),
]
