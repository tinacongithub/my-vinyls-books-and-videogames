from django import forms
from VinylsBooksVideoGames.models import Vinyls

class Search(forms.Form):
    title = forms.CharField(max_length=100)

class VinylsForm(forms.ModelForm):
  class Meta:
    model = Vinyls
    fields = ['title', 'artist', 'tracks']

