from django.conf.urls import url, include
from tenders_django_app.views import TendersView
from django.views.generic import TemplateView



urlpatterns = {
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^tenders/$', TendersView.as_view(), name="tenders"),
}
