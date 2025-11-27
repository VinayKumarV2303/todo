from django.db import models

class Task(models.Model):
    DEV_CHOICES = [
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

    developer = models.CharField(max_length=20, choices=DEV_CHOICES)
    title = models.CharField(max_length=255)
    week = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo",
    )

    class Meta:
        ordering = ["developer", "week", "day"]

    def __str__(self):
        return f"{self.get_developer_display()} – W{self.week}D{self.day}: {self.title}"
