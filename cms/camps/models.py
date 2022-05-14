from django.db import models

class CampModel(models.Model):
    __doc__ = "Model for camps"

    class CampType(models.TextChoices):
        HYBRID = ("HYBRID", "гибридная смена")
        ONLINE = ("ONLINE", "онлайн смена")
        OFFLINE = ("OFFLINE", "оффлайн смена")

    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    title = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=32, choices=CampType.choices, null=False)
    description = models.CharField(max_length=4096, null=True)
    picture = models.ImageField(upload_to="camps/", null=True)
