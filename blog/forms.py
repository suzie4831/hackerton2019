from django import forms
from .models import Dday,Team

class DdayForm(forms.ModelForm):
   class Meta:
      model= Dday
      fields = ('team', 'title', 'date')

class TeamForm(forms.ModelForm):
   class Meta:
      model=Team
      fields= ('t_name','t_class')