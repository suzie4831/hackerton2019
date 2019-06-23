from django import forms
from .models import Dday

class DdayForm(forms.ModelForm):
   class Meta:
      model= Dday
      fields = ('team', 'title', 'date')