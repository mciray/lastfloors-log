from django.db import models

class LogEntry(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    user = models.CharField(max_length=255, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.method} {self.path} - {self.status_code} by {self.user}"