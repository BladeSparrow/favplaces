from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title','description','place_type','location','rating','image']

    def clean_title(self):
        t = self.cleaned_data.get('title')
        if not t or not t.strip():
            raise forms.ValidationError('Назва не може бути порожня')
        return t

    def clean_rating(self):
        r = self.cleaned_data.get('rating')
        if r < 1 or r > 5:
            raise forms.ValidationError('Рейтинг має бути від 1 до 5')
        return r
