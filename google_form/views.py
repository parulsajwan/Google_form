import csv
import os
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from .models import Form, FormTemplate
from .serializers import FormDetailCreateSerializer, TemplateFormSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@method_decorator(csrf_exempt, name='dispatch')
class FormDetailCreateView(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormDetailCreateSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        try:
            data_dict = []
            serializer = FormDetailCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                name = serializer.data['name']
                file = serializer.data['file']
                new_file = file.replace('/', '\\')
                file_path = os.getcwd() + new_file
                csv_file_path = r"%s" % (file_path)
                print(csv_file_path)
                with open(csv_file_path, encoding='utf-8') as csv_file_handler:
                    csv_reader = csv.DictReader(csv_file_handler)
                    for rows in csv_reader:
                        data_dict.append(rows)
                context = {
                    'form_name': name,
                    'details': data_dict
                }
                for i in data_dict:
                    if i['type'] == 'singleSelect':
                        i['options'] = i['options'].split(', ')
                return render(request, 'forms/form.html', context)
        except Exception as e:
            return Response("Error: %s" % (repr(e)), status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class TemplateFormListCreateView(generics.ListCreateAPIView):
    queryset = FormTemplate.objects.all()
    serializer_class = TemplateFormSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        dict = {}
        try:
            for i in request.data:
                if i not in ['csrfmiddlewaretoken', 'Form_name']:
                    dict[i] = request.data[i]
            form_name = request.data['Form_name']
            details = dict
            data = FormTemplate.objects.create(
                form_name=form_name, template_data=details)
            serializer = TemplateFormSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("Error: %s" % (repr(e)), status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class TemplateFormRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormTemplate.objects.all()
    serializer_class = TemplateFormSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]
