from django import forms
from basket.models import Player,Team,Coach,Match,TeamCompose


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
        widgets = {
            'birthday': forms.DateInput(attrs={'class':'datepicker'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'logo','code']

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'age', 'email', 'nickname', 'team', 'rut', 'dv']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['name','team1','team2']
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }

class TeamComposeForm(forms.ModelForm):
    class Meta:
        model = TeamCompose
        fields = ["players","match"]

    players = forms.ModelMultipleChoiceField(queryset=Player.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['players'] = [t.pk for t in kwargs['instance'].topping_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.topping_set.clear()
        for player in self.cleaned_data['players']:
            instance.topping_set.add(player)