from django import forms

class QRCodeForm(forms.Form):
    name=forms.CharField(
        max_length=300,
        label="Name",
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'ENTER YOUR NAME'
            }));
    url=forms.URLField(
        max_length=500,
        label='URL',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'ENTER YOUR URL LINK'
        })
        );

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
