from django import forms

class BMIForm(forms.Form):
    height = forms.IntegerField(label='身長: ', initial=165)
    weight = forms.IntegerField(label='体重: ', initial=55)