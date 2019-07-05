from django import forms 
from django.forms import widgets
from review.models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    house_number = forms.IntegerField(label='House Number')
    street_name = forms.CharField(label='Address', max_length=100)
    location = forms.CharField(label='Location', max_length=50)
    review = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('user',)

    title.widget.attrs.update({'class': 'form-control', 
                               'placeholder': 'eg. Worst house I ever lived'})
    house_number.widget.attrs.update({'class': 'form-control', 
                               'placeholder': 'House Number'})
    street_name.widget.attrs.update({'class': 'form-control', 
                               'placeholder': 'eg. Kolawole street Yaba'})
    location.widget.attrs.update({'class': 'form-control', 
                               'placeholder': 'Lagos'})
    review.widget.attrs.update({'class': 'form-control'})

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)


class SearchForm(forms.Form):
    number = forms.IntegerField(label='House Number', required=False)
    address = forms.CharField(label='Address', max_length=100)
    location = forms.CharField(label='Location', max_length=50)

    number.widget.attrs.update({'class': 'form-control',
                               'placeholder': 'Number'})
    address.widget.attrs.update({'class': 'form-control',
                                 'placeholder': 'Street'})
    location.widget.attrs.update({'class': 'form-control',
                                  'placeholder': 'Area/state'})


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

    username.widget.attrs.update({'class': 'input--style-1', 
                               'placeholder': 'username'})
    email.widget.attrs.update({'class': 'input--style-1',
                                 'placeholder': 'email'})
    password.widget.attrs.update({'class': 'input--style-1',
                                  'placeholder': 'password'})

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', )

    username.widget.attrs.update({'class': 'input100"', 
                               'placeholder': 'username'})
    password.widget.attrs.update({'class': 'input100"',
                                  'placeholder': 'password'})