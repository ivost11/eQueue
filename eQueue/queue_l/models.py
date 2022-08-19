from django.db import models
from django.urls import reverse


class QueueL(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(blank=True, verbose_name='Description')
    email = models.EmailField(max_length=254, verbose_name='E-Mail')
    count = models.IntegerField(verbose_name='Count'),
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)

    def get_absolute_url(self):
        return reverse('view_queue', kwargs={"queue_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Queue'
        verbose_name_plural = 'Queues'
        ordering = ['-created_at']
