from django import forms
from basket.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
        widgets = {
            'birthday': forms.DateInput(attrs={'class':'datepicker'}),
        }
