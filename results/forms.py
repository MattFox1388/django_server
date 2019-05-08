from django import forms


class SearchForm(forms.Form):

    search_phrase = forms.CharField(max_length=128)
    CHOICES = (('Search By Keyword', 'Search By Keyword'), ('Search By Tag', 'Search By Tag'),)
    search_by = forms.ChoiceField(choices=CHOICES)
