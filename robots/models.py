from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=True, null=True)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)

    @property
    def quantity(self) -> int:
        return Robot.objects.filter(model=self.model, version=self.version).count()
