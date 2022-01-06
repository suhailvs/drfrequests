from django.urls import path
from rest_framework_requests.views import DRFDocsView

urlpatterns = [
    # Url to view the API Docs
    path('', DRFDocsView.as_view(), name='drfdocs'),
]
