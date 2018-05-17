from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'   # When the user comes in ready to signup, we are going to call
        # UserCreationForm from .auth.forms then meta class is set up to show the fields for login. If we want labels on
        # that form we set up the init method. This is similar (init method) to actually setting in the html file.
        self.fields['email'].label = 'Email Address'

