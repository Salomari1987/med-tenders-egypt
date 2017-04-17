from django.conf.urls import url, include
from tenders_django_app.views import TendersView


urlpatterns = {
    url(r'^tenders/$', TendersView.as_view(), name="tenders"),
}
