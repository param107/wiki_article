from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Article


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()

        return user


class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=('title','body','pub_date','thumbnail','is_private')



