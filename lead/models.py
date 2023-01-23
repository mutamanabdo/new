from django.db import models
from django.contrib.auth.models import User

class lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    PRAIORITY_STATUS = (
        (LOW, 'Low'),
        (MEDIUM , 'Medium'),
        (HIGH , 'High'),
        )
    CONTACTED = 'contacted'
    WIN = 'win'
    LOST = 'lost'
    NEW = 'new'

    STATUS_CHOICE= (
        (WIN, 'Win'),
        (LOST, 'Lost'),
        (CONTACTED, 'Contacted'),
        (NEW, 'New'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=15, choices=PRAIORITY_STATUS, default=MEDIUM)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default=NEW)
    converted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name