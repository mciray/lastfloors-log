from django.urls import path,re_path
from .views import LogEntryListView, LogEntryCreateView, user_login,index


urlpatterns = [
    path('login', user_login, name='login'),
    path('',index, name='home'),
    path('list/', LogEntryListView.as_view(), name='log-entry-list'),
    path('create/', LogEntryCreateView.as_view(), name='log-entry-create'),
]