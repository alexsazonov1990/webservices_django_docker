from django import forms
from .models import ApplicationForDevelopmentCard
from .models import MyModel
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = ApplicationForDevelopmentCard
        fields = ('topic', 'purpose', 'why_necessary', 'why_use_it', 'where_used', 'full_name_customer', 'email',)


class AttachForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('upload',)

    '''
        exclude = ['headline']
        topic = forms.CharField(max_length=100,
                               widget=forms.TextInput
                                (attrs={'placeholder': 'Enter your first name'}))
        purpose = forms.CharField(max_length=100,
                                  widget=forms.EmailInput
                                  (attrs={'placeholder': 'Enter your email'}))
        why_necessary = forms.CharField(max_length=100,
                                        widget=forms.TextInput
                                        (attrs={'placeholder': '(xxx)xxx-xxxx'}))

# class Meta:
# model = ApplicationForDevelopmentCard

# fields = '__all__'

#  fields = ('topic', 'purpose', 'why_necessary', 'why_use_it', 'where_used', 'full_name_customer', 'email',)
'''
