from django import forms
from AppThree.models import User


class NewUserForm(forms.ModelForm):   # before using the form and use model to edit the data .ModelForm is used
    class Meta:     # Inline class refers to Meta class
        model = User  # model attribute
        fields = '__all__'  # __all__ grabs all fields

