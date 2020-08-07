from django.db import models


class TaskItem(models.Model):
    title = models.CharField(max_length=200)
    status_completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
