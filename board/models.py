from django.db import models

class Task(models.Model):
    ASSIGNEE_CHOICES = [
        ("vinay", "Vinay Kumar V"),
        ("yashwanth", "Yashwanth H V"),
        ("shashanka", "Shashanka S"),
        ("lakshmana", "Lakshmana M R"),
    ]

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255)
    assignee = models.CharField(max_length=20, choices=ASSIGNEE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    day = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} → {self.assignee} ({self.status})"
