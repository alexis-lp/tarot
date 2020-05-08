from django import forms
from .models import *

class newPlayerForm(forms.ModelForm):
    class Meta:
        model = TarotPlayer
        fields = ['player',]

class newGameForm(forms.ModelForm):

    class Meta:
        model = TarotGame
        fields = ['player1','player2','player3','player4','player5',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player1'].widget.attrs.update({'class': 'form-control'})
        self.fields['player2'].widget.attrs.update({'class': 'form-control'})
        self.fields['player3'].widget.attrs.update({'class': 'form-control'})
        self.fields['player4'].widget.attrs.update({'class': 'form-control'})
        self.fields['player5'].widget.attrs.update({'class': 'form-control'})

