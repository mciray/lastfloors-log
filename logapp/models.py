from django.db import models

class LogEntry(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    user = models.CharField(max_length=255, default='Anonymous')
    response_time= models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code} by {self.user}"