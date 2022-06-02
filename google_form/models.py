from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    file = models.FileField(upload_to='upload/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FormTemplate(models.Model):
    form_name = models.CharField(max_length=150, blank=False, null=False)
    template_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.form_name
