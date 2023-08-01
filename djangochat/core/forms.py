from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# The `SignUpForm` class is a subclass of `UserCreationForm` that is used for creating a new user with
# a username and password.
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']