from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    created_add = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta():
        # ordernar pela data de entrega
        ordering = ["deadline"]

    def mark_as_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
