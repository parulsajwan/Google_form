from django.urls import path, include

from . import views

# for  Products
urlpatterns = [
    path('', views.FormDetailCreateView.as_view(), name="form_details"),
    path('', views.TemplateFormListCreateView.as_view(), name="form_post"),
    path('', views.TemplateFormRetrieveUpdateDestroyView.as_view(), name="form_update"),
]
