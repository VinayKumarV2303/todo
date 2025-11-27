from django.db import models


class Task(models.Model):
    DEVELOPER_CHOICES = [
        ("vinay", "Vinay"),
        ("yashwanth", "Yashwanth"),
        ("shashana", "Shashana"),
        ("lakshman", "Lakshman"),
    ]

    STATUS_CHOICES = [
        ("todo", "To-Do"),
        ("progress", "In Progress"),
        ("review", "Review"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=20, choices=DEVELOPER_CHOICES)
    week = models.IntegerField()
    day = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")

    def __str__(self):
        return f"{self.developer} - {self.title}"
