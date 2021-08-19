
# from django.db.models import fields
from django.forms import ModelForm
from products.widgets import CustomClearableFileInput
from .models import Testimonial
from django import forms


class CustomerTestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        labels = {
            'name' : '',
            'email' : '',
            'your_thoughts' : '',
            'upload_image' : '',
            'twitter_link' : '',
            'linkedin_link' : '',
            'facebook_link' : '',
            'instagram_link' : '',
            'other_social_media_link' : '',
        }
        fields = (
            'name',
            'email',
            'your_thoughts',
            'twitter_link',
            'linkedin_link',
            'facebook_link',
            'instagram_link',
            'other_social_media_link',
            'upload_image',
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Name'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Email'}),
            'your_thoughts' : forms.Textarea(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Your Thoughts?'}),
            'twitter_link' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'twitter_link'}),
            'linkedin_link' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'linkedin_link'}),
            'facebook_link' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'facebook_link'}),
            'instagram_link' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'instagram_link'}),
            'other_social_media_link' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'other_social_media_link'}),
            # 'upload_image' : forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput),

        }
