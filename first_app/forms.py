from django import forms
from django.core import validators
from first_app.models import User, UserProfileInfo
from django.contrib.auth.models import User as AdminUser

class FormName(forms.Form):
    name = forms.CharField(validators=[])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[
    #                              validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')

class NewUser(forms.ModelForm):
    class Meta():
        model = AdminUser
        fields = ('username','email','password')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = AdminUser
        fields = ('username', 'email', 'password')

class UserProfileInform(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
