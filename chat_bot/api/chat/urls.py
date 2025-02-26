from django.urls import path
from .views import test_azure, upload_pdf, query_rag

urlpatterns = [
    path("upload-pdf/", upload_pdf, name="upload_pdf"),
    path("query-rag/", query_rag, name="query_rag"),
    path("test-azure/", test_azure, name="test_azure"),
]