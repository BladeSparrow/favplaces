from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Place(models.Model):
    TYPE_CHOICES = [
        ('restaurant','Restaurant'),
        ('bar','Bar'),
        ('park','Park'),
        ('cinema','Cinema'),
        ('other','Other'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    place_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='other')
    location = models.CharField(max_length=200, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='places/', blank=True, null=True)

    class Meta:
        ordering = ['-rating', '-created_at']

    def short_description(self, n=40):
        return (self.description[:n] + '...') if len(self.description) > n else self.description

    def __str__(self):
        return self.title
>>>>>>> 05b0b54 (Lab implementation: models, views, templates, cleanup)
