from django.urls import path, include
from . import views

urlpatterns = [
    # ... other URLs
    path('excel-to-csv/', views.ExcelToCSVView.as_view(), name='excel_to_csv'),
    #path('download-csv/<str:file_path>/', views.download_csv),
]
