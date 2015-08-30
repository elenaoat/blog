from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse_lazy
from crispy_forms.layout import Submit, HTML

class PostForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.form_action = reverse_lazy('add_post')
    class Meta:
        model = Post
        exclude = ['pub_date', 'slug']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('add_post')
        self.helper.layout.append(FormActions(Submit('save', 'Submit'),
        ))