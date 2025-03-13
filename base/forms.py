from django.forms import ModelForm
from .models import Room


class RomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'