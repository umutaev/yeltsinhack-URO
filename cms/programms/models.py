from django.db import models

class ProgrammModel(models.Model):
    __doc__ = "Model for programs"

    class CampType(models.TextChoices):
        ONLINE = ("ONLINE", "Online")
        OFFLINE = ("OFFLINE", "Offline")

    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    title = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=32, choices=CampType.choices, null=False)
    description = models.CharField(max_length=4096, null=True, blank=True)
    picture = models.ImageField(upload_to="programms/", null=True, blank=True)

    def __str__(self):
        return f'{self.get_type_display().capitalize()} программа "{self.title}" с {self.start_date} по {self.end_date}'
