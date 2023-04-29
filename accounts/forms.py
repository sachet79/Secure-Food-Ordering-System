from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


# Password Validation
def validate_password_special_characters(password):
    """
   Validator function to check that a password contains contain special characters
    """ 
    if not any(char in password for char in "!@#$%^&*()_+-="):
        raise ValidationError(
            _("The password must contain at least one of the following special characters: !@#$%^&*()_+-="),
            code='password_no_special_characters',
        )

 # First name & Last name validation   
def validate_no_special_characters(fnamelname):
    """
    Validator function to check that a string doesn't contain special characters
    """
    special_characters = '!@#$%^&*()_+-='
    if any(char in special_characters for char in fnamelname):
        raise ValidationError(
            _("The input field should not contain any special characters."),
            code='no_special_characters',
        )    

class NewUSerForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])
    phone_number = PhoneNumberField()
    first_name = forms.CharField(required=True, validators=[validate_no_special_characters])
    last_name = forms.CharField(required=True, validators=[validate_no_special_characters])

    

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password' }),
        validators=[validate_password_special_characters],
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
        strip=False,
    )    
    
    #email already registered
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("The given email is already registered")
        return self.cleaned_data['email']



    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2")

    def save(self,commit=True):
        user = super(NewUSerForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

#captcha implementation
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

 