from django import forms
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    template_name = 'edit_profile.html'

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'

        )
        widgets = {  # Add 'required' attribute to required fields
            'username': forms.TextInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.Textarea(attrs={'required': True}),
            'email': forms.Textarea(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update(
                {'class': 'form-control'})
