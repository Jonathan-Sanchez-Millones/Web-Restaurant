from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()

class MyUserForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('nombres','apellidos','address','email') #'full_name',)

    def clean_password(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        
        return password

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MyUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
