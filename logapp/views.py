from .models import LogEntry
from django.shortcuts import render
from .serializers import LogEntrySerializer
from rest_framework import generics
from .models import LogEntry
from .serializers import LogEntrySerializer
import requests

class LogEntryListView(generics.ListAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

class LogEntryCreateView(generics.CreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

def index(request):
    
    return render(request,'index.html')

