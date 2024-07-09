from .models import LogEntry
from .serializers import LogEntrySerializer
from rest_framework import generics
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from loglama.settings import POST_SECRET
from django.db.models import Q

class LogEntryListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogEntrySerializer

    def get_queryset(self):
        queryset = LogEntry.objects.all()

        # Filtreleme seçeneklerini al
        path = self.request.query_params.get('path', None)
        method = self.request.query_params.get('method', None)
        status_code = self.request.query_params.get('status_code', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        user = self.request.query_params.get('user', None)

        # Eğer en az bir filtreleme seçeneği belirtilmişse, bütün modelde arama yap
        if path or method or status_code or start_date or end_date or user:
            filter_conditions = Q()
            if path:
                filter_conditions &= Q(path__icontains=path)
            if method:
                filter_conditions &= Q(method__icontains=method)
            if status_code:
                filter_conditions &= Q(status_code=status_code)
            if start_date:
                filter_conditions &= Q(created_at__gte=start_date)
            if end_date:
                filter_conditions &= Q(created_at__lte=end_date)
            if user:
                filter_conditions &= Q(user__icontains=user)
            queryset = queryset.filter(filter_conditions)
        else:
            # Hiçbir filtreleme yapılmadığında son 50 kayıt getirilsin
            last_entries = list(reversed(queryset.order_by('-created_at')[:50]))
            return last_entries

        return queryset
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


def custom_404_view(request):
    return render(request, '404.html')