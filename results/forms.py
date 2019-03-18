from django import forms

FILE_CHOICES = (
    ('text', 'TEXT'),
    ('audio', 'AUDIO'),
    ('video', 'VIDEO'),
    ('images', 'IMAGES')
)

class SearchForm(forms.Form):
    search_phrase = forms.CharField(max_length=128)
    files = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FILE_CHOICES)
