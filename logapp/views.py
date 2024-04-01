from .models import LogEntry
from .serializers import LogEntrySerializer
from rest_framework import generics
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from loglama.settings import POST_SECRET
from django.db.models import Q
class LogEntryListView(generics.ListAPIView):
    serializer_class = LogEntrySerializer
    def get_queryset(self):
        queryset = LogEntry.objects.order_by('created_at')
        
        
        # Filtreleme seçeneklerini al
        path = self.request.query_params.get('path', None)
        method = self.request.query_params.get('method', None)
        status_code = self.request.query_params.get('status_code', None)

        # Filtreleme seçeneklerine göre queryset'i filtrele
        if path:
            queryset = queryset.filter(path__icontains=path)
        if method:
            queryset = queryset.filter(method__icontains=method)
        if status_code:
            queryset = queryset.filter(status_code=status_code)

        last_entry = queryset.last()
        return queryset.exclude(pk=last_entry.pk)[:49] | queryset.filter(pk=last_entry.pk)

class LogEntryCreateView(generics.CreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    def post(self, request, *args, **kwargs):
        secure_key = request.headers.get('X-Custom-Secure-Key')
        if secure_key != POST_SECRET:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def index(request):
    return render(request,'index.html')

