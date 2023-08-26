from django.db import models

class DocumentTemplate(models.Model):
    name = models.CharField(blank=True, null= True, max_length=200)
    template_text = models.TextField(blank=True)
    template_document = models.FileField(blank=True, null=True, upload_to='todo/', storage=None)
    data_text = models.TextField(blank=True)
    data_document = models.FileField(blank=True, null=True)
    format = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'

    def __str__(self):
        return self.name

