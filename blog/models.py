from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # using charfield because we want to limit the number of characters in a summary
    summary = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def wrapped_text(self):
        MAX_NUMBER_OF_CHARS = 200
        if len(self.text) > MAX_NUMBER_OF_CHARS:
            return self.text[:MAX_NUMBER_OF_CHARS] + "..."
        else:
            return self.text

    def __str__(self):
        return self.title