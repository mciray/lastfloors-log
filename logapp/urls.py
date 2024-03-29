from django.urls import path
from .views import LogEntryListView, LogEntryCreateView,index

app_name='log/'

urlpatterns = [
    path("", index, name="home"),
    path('list/', LogEntryListView.as_view(), name='log-entry-list'),
    path('create/', LogEntryCreateView.as_view(), name='log-entry-create'),

    
]
