from django import forms
from .models import Part

class AddPart(forms.ModelForm):

    class Meta:
        model = Part
        fields = (
        'type',
        'status',
        'location',
        'size',
        'serial',
        'model',
        'brand',
        'description',
        'shipping',
        'po_number',
        )
