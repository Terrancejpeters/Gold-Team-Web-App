from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
	input_text = forms.CharField(help_text="Enter a post less than 256 characters",max_length= 256, min_length = 1)
	
	def clean_post_text(self):
		data = self.cleaned_data['input_text']
		
		return data
	
def submitPost(PostForm):
	if PostForm.method == 'POST':
		form = PostForm()
		if form.is_valid():
			form.save()
			return HTTPResponseRedirect(reverse(''))
		else:
			messages.error(PostForm, "Error")

	return render(PostForm, '/', {'form': PostForm()})