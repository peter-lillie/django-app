from django import forms

from .models import SignupModel


class SignupForm(forms.ModelForm):

    class Meta:
        model = SignupModel
        fields = "__all__"