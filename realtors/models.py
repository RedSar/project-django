from django.db import models


class Realtor(models.Model):
    """Model definition for Realtor."""

    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/realtors/')
    description = models.TextField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField()

    class Meta:
        """Meta definition for Realtor."""

        verbose_name = 'Realtor'
        verbose_name_plural = 'Realtors'

    def __str__(self):
        """Unicode representation of Realtor."""
        pass
