from django import forms
from company.models import CompanyModel, Job


class CompanyProfileForm(forms.ModelForm):

    company_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Name'}
    ), required = True, max_length = 100)

    company_field = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Field'}
    ), required = True, max_length = 100)

    company_email = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Email'}
    ), required = True, max_length = 100)

    comapany_country = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Country Name'}
    ), required = True, max_length = 100)

    company_contact = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Contact','type':'tel'}
    ), required = True, max_length = 10)

    company_description = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Company Description', 'rows':'7'}
    ), required = True, max_length = 400)

    class Meta:
        model = CompanyModel
        exclude = ('user',)

class JobForm(forms.ModelForm):

    company_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Name'}
    ), required = True, max_length = 100)

    company_website = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Website'}
    ), required = True, max_length = 100)

    company_email = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Company Email'}
    ), required = True, max_length = 100)

    job_location = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Job Location'}
    ), required = True, max_length = 100)

    job_vacancy = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Vacancy', 'type':'number'}
    ), required = True, max_length = 100)

    date_from = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Start Date', 'type':'date'}
    ), required = True)

    date_till = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Last Date', 'type':'date'}
    ), required = True)

    job_description = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Job Description', 'rows':'6'}
    ), required = True, max_length = 400)

    salary = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Salary', 'type':'number'}
    ), required = True, max_length = 30)

    perks = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Perks seperated by , eg:Casual Dress,Snacks '}
    ), required = True, max_length = 300)

    class Meta:
        model = Job
        widgets = {
            'job_profile':forms.RadioSelect(),
            'job_type':forms.RadioSelect(),
        }
        exclude = ('user','posted_date')
