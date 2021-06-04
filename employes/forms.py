from django import forms


class DepForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    intitule = forms.CharField(label='intitulé', max_length=30)
    etage = forms.IntegerField()

    def is_valid(self):
        return True
