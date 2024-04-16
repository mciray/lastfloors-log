from django.db import models

class LogEntry(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    user = models.CharField(max_length=255, default='Anonymous')
    response_time = models.FloatField(blank=True)
    ip_address = models.CharField(max_length=45, blank=True)
    query_params = models.JSONField(blank=True, null=True)
    exception = models.TextField(blank=True)
    traceback = models.TextField(blank=True)
    file_name = models.CharField(max_length=255, blank=True)
    line_number = models.IntegerField(blank=True, null=True)
    function_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code} by {self.user}"
