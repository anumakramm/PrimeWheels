from django import forms
from carapp.models import OrderVehicle

class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'vehicles_ordered']
        widgets = {
            'buyer': forms.Select()
        }
        labels = {
            'vehicles_ordered': 'Number of Vehicles Ordered'
        }

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')