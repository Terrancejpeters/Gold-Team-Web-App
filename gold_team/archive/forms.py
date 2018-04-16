from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	input_text = forms.CharField(help_text = "Enter a post less than 256 characters",max_length= 256, min_length = 1)

