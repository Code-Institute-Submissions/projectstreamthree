from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


# Code taken from Code Institute Lesson
class UserRegistrationForm(UserCreationForm):
    "Registration form taking email and password"
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)
        return email


class UserSubscriptionForm(forms.ModelForm):
    "Stripe subscription form"
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2017, 2036)]
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'stripe_id']
        exclude = ['username']

    def save(self, commit=True):
        instance = super(UserSubscriptionForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance


class UserLoginForm(forms.Form):
    "Log in form"
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
