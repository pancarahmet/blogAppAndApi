from django.forms import ModelForm
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']