# Google_form

**Design and implement a service like Google Forms:**

    1. Users can create a form template by defining a form name & defining the form fields.
    2. The form fields are defined using a csv file (image attached below). The form fields will be defined by following parameters:
        Field_name: Specifying the name of the field
        Type: The front-end will collect data as this type of entry
              Text
              Single select
              Number
              Date
        Options: Only for single select type, null for other types. Mentions values to show amongst which a single selection will be made.
        Mandatory: Whether it is mandatory to enter data in that field or not (a condition for the front-end to check before form submission)
    3. Once a form template is created, users can fill the form multiple times creating multiple form entries
    4. Users can create, update, delete entries for a form template


**Tech Stack**
Django
Django rest framework
Mongodb
HTML
CSS
BOOTSTRAP


**<!-- API Usages: -->**

**FormDetailCreateView -- **
          Endpoint : /form/create/
          Mehthod : POST
          Description : **This API is for creating the template, it take form name and csv file as a input for creating template form.
          This API save the form details and return to Template created. **
          
**TemplateFormListCreateView --**
          Endpoint : /form/template/
          Mehthod : GET, POST
          Description : **This API is for Creating the entries for the Template form and for see the list of all the forms entries created so far.**
       
**TemplateFormRetrieveUpdateDestroyView ---**
          Endpoint : /form/template/id
          Mehthod : GET,PUT,PATCH,DELETE
          Description : **This API is for getting the details of template form by id , we can update the data of template form and also delete the entry.**
          

