from django import forms

class SearchForm(forms.Form):
    search_phrase = forms.CharField(max_length=128)
