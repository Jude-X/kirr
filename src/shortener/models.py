from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.


class KirrURL(models.Model):
    url = models.CharField(max_length=220, unique=True)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    def __repr__(self):
        return f'<{self.url} - {self.shortcode}>'
