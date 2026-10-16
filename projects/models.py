

from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('Tayyor', 'Tayyor'),
        ('Ishlab chiqilmoqda', 'Ishlab chiqilmoqda'),
        ('Rejada', 'Rejada'),
    ]

    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    description = models.TextField(verbose_name="Batafsil tavsifi")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ishlab chiqilmoqda', verbose_name="Holati")
    technologies = models.JSONField(default=list, verbose_name="Texnologiyalar")  # Masalan: ["Python", "Django", "PostgreSQL"]
    github_link = models.URLField(blank=True, null=True, verbose_name="GitHub havola")
    live_link = models.URLField(blank=True, null=True, verbose_name="Demo havola")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title