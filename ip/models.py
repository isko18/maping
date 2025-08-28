from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} ({self.latitude}, {self.longitude}) @ {self.visited_at}"
    
    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"

class Image(models.Model):
    image = models.ImageField(upload_to="image/", verbose_name="Изображение", null=True, blank=True)
    
    def __str__(self):
        return str(self.image)
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображении"
