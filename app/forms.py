from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    invitation_code = forms.CharField(max_length=100, required=True, label='Invitation Code')

    def clean_invitation_code(self):
        code = self.cleaned_data['invitation_code']
        # Add your logic to validate the invitation code
        if code != "VALID_CODE":  # Replace with your actual validation logic
            raise forms.ValidationError("Invalid invitation code.")
        return code

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Add any additional logic here
        return user