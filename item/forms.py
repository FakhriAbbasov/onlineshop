from django import forms
from .models import Item
SMALL = 'py-4 px-6 rounded-xl border'
DESCRIPTION = 'py-4 px-6 rounded-xl border h-20'
class newItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': SMALL
            }),
            'name': forms.TextInput(attrs={
                'class': SMALL
            }),
            'description': forms.Textarea(attrs={
                'class': DESCRIPTION
            }),
            'price': forms.TextInput(attrs={
                'class': SMALL
            }),
            'image': forms.FileInput(attrs={
                'class': SMALL
            })
        }

class editItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': SMALL
            }),
            'description': forms.Textarea(attrs={
                'class': SMALL
            }),
            'price': forms.TextInput(attrs={
                'class': SMALL
            }),
            'image': forms.FileInput(attrs={
                'class': SMALL
            })
        }