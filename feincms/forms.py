from django import forms


class MediaFileTranslationForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea)
