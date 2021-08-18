
from django.db.models import fields
from django.forms import ModelForm
from .models import Testimonial
from django import forms


class CustomerTestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        labels = {
            'full_name' : '',
            'your_thoughts' : '',
            'twitter_link' : '',
            'linkedin_link' : '',
            'facebook_link' : '',
            'instagram_link' : '',
            'other_social_media_link' : '',
        }
        fields = (
            'full_name',
            'your_thoughts',
            'twitter_link',
            'linkedin_link',
            'facebook_link',
            'instagram_link',
            'other_social_media_link',
        )
        widgets = {
            'full_name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'full_name'}),
            'your_thoughts' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'your_thoughts'}),
            'twitter_link' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'twitter_link'}),
            'linkedin_link' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'linkedin_link'}),
            'facebook_link' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'facebook_link'}),
            'instagram_link' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'instagram_link'}),
            'other_social_media_link' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'other_social_media_link'}),

        }
