from allauth.account.forms import SignupForm, LoginForm
from django import forms
# from invitations.models import Invitation


# class CustomLoginForm(LoginForm):
#     remember = None  # Hides the 'remember me' field


# class CustomSignupForm(SignupForm):
#     invitation_code = forms.CharField(max_length=100, required=True, label='Invitation Code')

#     def clean_invitation_code(self):
#         code = self.cleaned_data['invitation_code']
#         try:
#             invitation = Invitation.objects.get(key=code)
#             if invitation.is_accepted:
#                 raise forms.ValidationError("This invitation code has already been used.")
#         except Invitation.DoesNotExist:
#             raise forms.ValidationError("Invalid invitation code.")
#         return code

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         code = self.cleaned_data['invitation_code']
#         invitation = Invitation.objects.get(key=code)
#         invitation.accepted = True
#         invitation.save()
#         return user