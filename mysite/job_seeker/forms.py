from django import forms
from job_seeker.models import UserModel, Project, Skill, Award, Certification

class UserModelForm(forms.ModelForm):

    full_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Full Name'}
    ), required = True, max_length = 100)

    user_email = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'User Email'}
    ), required = True, max_length = 100)

    # gender = forms.ChoiceField(widget = forms.Select(
    #     choices = (('Male','Male'), ('Female','Female'))
    # ), required = True)

    date_of_birth = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Date of Birth', 'type':'date'}
    ), required = True)

    mobile_number = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Mobile Number', 'type':'number'}
    ), required = True, max_length = 100)

    # options radio buttons

    address_line1 = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Address Line 1'}
    ), required = True, max_length = 100)

    address_line2 = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Address Line 2'}
    ), max_length = 100)

    city = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'City'}
    ), required = True, max_length = 100)

    state = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'State'}
    ), required = True, max_length = 100)

    zip = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Pincode', 'type':'number'}
    ), required = True, max_length = 100)

    tenth_institution = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Tenth School'}
    ), required = True, max_length = 100)

    tenth_board = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Tenth Board'}
    ), required = True, max_length = 100)

    tenth_result = forms.DecimalField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Tenth Result'}
    ), required = True, max_digits = 5)

    tenth_date = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Tenth completion', 'type':'date'}
    ), required = True)

    twelfth_institution = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Twelfth School'}
    ), required = True, max_length = 100)

    twelfth_board = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Twelfth Board'}
    ), required = True, max_length = 100)

    twelfth_result = forms.DecimalField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Twelfth Result'}
    ), required = True, max_digits = 5)

    twelfth_date = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Twelfth completion date', 'type':'date'}
    ), required = True)

    diploma_institution = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Diploma Institute'}
    ),required = False, max_length = 100)

    diploma_board = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Board'}
    ),required = False, max_length = 100)

    diploma_result = forms.DecimalField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Result'}
    ),required = False, max_digits = 5)

    diploma_date = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Passing Date','type':'date'}
    ),required = False)

    bachelor_institution = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Institute Name'}
    ), required = True, max_length = 100)

    bachelor_board = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Board Name'}
    ), required = True, max_length = 100)

    bachelor_program = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Program Name'}
    ), required = False, max_length = 100)

    bachelor_stream = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Stream'}
    ),required = False, max_length = 100)

    bachelor_result = forms.DecimalField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Bachelor Result'}
    ), required = True, max_digits = 5)

    bachelor_date = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Passing Date', 'type':'date'}
    ), required = True)

    resume_headline = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Your Resume Headline', 'rows':'3'}
    ), required = True, max_length = 200)

    extra_curriculam = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Type items seperated by comma eg: Debate, Elocution ', 'rows':'7'}
    ), required = True, max_length = 500)

    hobies = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Type items seperated by comma eg: Cooking,Reading ', 'rows':'7'}
    ), required = True, max_length = 500)


    class Meta:
        model = UserModel
        exclude = ('user',)

class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Project Name'}
    ), required = True, max_length = 100)

    project_link = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Project Link'}
    ), required = True, max_length = 100)

    project_description = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Project Description', 'rows':'7'}
    ), required = True, max_length = 100)

    start_date =  forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Start Date', 'type':'date'}
    ), required = True, max_length = 100)

    end_date = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'End Date', 'type':'date'}
    ), required = True, max_length = 100)


    class Meta:
        model = Project
        exclude = ('user',)

class SkillForm(forms.ModelForm):

    skill_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Skill Name'}
    ), required = True, max_length = 100)

    class Meta:
        model = Skill
        exclude = ('user',)

class AwardForm(forms.ModelForm):
    award_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Award Name'}
    ), required = True, max_length = 100)

    award_organization = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Organization Name'}
    ), required = True, max_length = 100)

    award_description = forms.CharField(widget = forms.Textarea(
        attrs = {'class':'form-control', 'placeholder':'Award Description', 'rows':'7'}
    ), required = True, max_length = 100)

    class Meta:
        model = Award
        exclude = ('user',)


class CertificationForm(forms.ModelForm):
    certification_name = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Certification Name'}
    ), required = True, max_length = 100)

    certification_organization = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Organization Name'}
    ), required = True, max_length = 100)

    certificate_link = forms.CharField(widget = forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'Certificate Link'}
    ), required = True, max_length = 100)

    valid_from = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Passing Date', 'type':'date'}
    ), required = True)

    valid_till = forms.DateField(widget = forms.DateInput(
        attrs = {'class':'form-control', 'placeholder':'Passing Date', 'type':'date'}
    ), required = True)

    class Meta:
        model = Certification
        widgets = {
            'valid_from': forms.SelectDateWidget(),
            'valid_till' : forms.SelectDateWidget(),
        }
        exclude = ('user',)
