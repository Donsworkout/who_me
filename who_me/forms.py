from django import forms

from .models import FaceInfo

class FaceInfoForm(forms.ModelForm):

    class Meta:
        model = FaceInfo
        fields = ('title', 'text',)