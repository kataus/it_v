from django import forms
from django.forms import ModelForm

from .models import Article


class ArticleForm(forms.ModelForm):
    prev_image = forms.ImageField(label='Картинка на заголовке', required=False)

    def __init__(self, *args, **kw):
        super(ModelForm, self).__init__(*args, **kw)
        self.fields.keyOrder = [
            'label',
            'prev_image',
            'description',
            'text']

    class Meta:
        model = Article
        fields = ['label', 'description', 'text']
        labels = {'label': 'Заголовок', 'description': 'Описание/Summary', 'text': 'Текст страницы'}
        widgets = {'text': forms.Textarea(attrs={'cols': '150', 'rows': '30'}),
                   'description': forms.Textarea(attrs={'cols': '150', 'rows': 5})}