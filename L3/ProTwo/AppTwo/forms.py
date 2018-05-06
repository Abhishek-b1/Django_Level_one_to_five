# from django import forms
#
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with z')
#
#
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
#     required=False because to inspect the html page and catch the internet bot
#
#     def clean_botcatcher(self):
#         botcatcher = self.cleaned_data['botcatcher']
#         if len(botcatcher) > 0:
#             raise forms.ValidationError("Gotcha BOT!")
#         return botcatcher

#########_____ z validator ______________###############

# from django import forms
# from django.core import validators
#
#
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with z')
#
#
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)
#                                                                                        ])

################### Email verification process
from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your Email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):   # To clean the data
        all_clean_data = super(FormName, self).clean()   # This will return all cleaned data for the entire form
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure emails match!")





