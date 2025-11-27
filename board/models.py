from django.db import models

class Task(models.Model):
    ASSIGNEE_CHOICES = [
        ("vinay", "Vinay"),
        ("yashwanth", "Yashwanth"),
        ("shashana", "Shashana"),
        ("lakshman", "Lakshman"),
    ]

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assignee = models.CharField(max_length=20, choices=ASSIGNEE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} → {self.assignee} ({self.status})"
