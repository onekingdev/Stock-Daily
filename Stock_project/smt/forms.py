from django.forms import ModelForm
from .models import trails
from django import forms
from nsetools import Nse
from BuyTips.models import UserEmail

class forr(ModelForm):
    class Meta:
        model = trails
        fields = "__all__"
        nse = Nse()
        all_stock_codes = nse.get_stock_codes()
        trai = tuple((n, m) for n, m in all_stock_codes.items())
        widgets = {
        'stocks': forms.CheckboxSelectMultiple(choices=trai),
        }
class Tips_Form(ModelForm):
    class Meta:
        model = UserEmail
        fields = "__all__"