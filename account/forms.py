from django.forms import EmailField
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(label=("Email address"), required=True,
                       help_text=("Required."))

    class Meta:
        model = Profile
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
