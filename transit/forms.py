from .models import Line, LINE_COLORS
from django import forms

class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = {'name'}

class LineChoices(forms.Form):
    line1 = forms.ModelChoiceField(
        queryset=Line.objects.all(),
        empty_label='Select beginning line',
        to_field_name='name',
    )
    #line2 = forms.ModelChoiceField(
    #    queryset=Line.objects.all(),
    #    empty_label='Select destination line',
    #    to_field_name='color',
    #)