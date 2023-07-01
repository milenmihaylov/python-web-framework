from django import forms

from templates_advanced.profiles.models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'age': forms.NumberInput(attrs={'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'custom-file-input'}),
		}
		exclude = ('user', 'is_complete')  # we don't what to change the user

