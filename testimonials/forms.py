
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
        }
        fields = (
            'name',
            'email',
            'your_thoughts',
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Name'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Email'}),
            'your_thoughts' : forms.Textarea(attrs={'class' : 'form-control col-md-12', 'placeholder' : 'Your Thoughts?'}),
            # 'upload_image' : forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput),

        }
