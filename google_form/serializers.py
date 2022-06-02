from rest_framework import serializers
from .models import Form, FormTemplate


class FormDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class TemplateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = '__all__'