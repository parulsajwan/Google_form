from django.urls import path, include

from . import views

# for  Products
urlpatterns = [
    path('create/', views.FormDetailCreateView.as_view(), name="form_details"),
    path('template/', views.TemplateFormListCreateView.as_view(), name="form_post"),
    path('template/<int:pk>/',
         views.TemplateFormRetrieveUpdateDestroyView.as_view(), name="form_update"),
]
