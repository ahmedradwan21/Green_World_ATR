from django.db import models

class Inquiry(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question[:50]}..."

    class Meta:
        verbose_name_plural = "Inquiries"
