import csv
from django.http import HttpResponse
#from rest_framework.parsers import FileUploadParser
import requests
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlretrieve
import openpyxl

class ExcelToCSVView(APIView):

    def post(self, request, format=None):
        excel_link = request.data.get ('url')
        # Download the Excel file from the link
        response = requests.get (excel_link)
        # Read the Excel file content and convert it to a CSV file
        df = pd.read_excel (response.content, engine='openpyxl')
        csv_file = df.to_csv (index=False)
        # Return the CSV file as a response
        response = HttpResponse (csv_file, content_type='text/csv')
        response ['Content-Disposition'] = 'attachment; filename="converted.csv"'
        return response
