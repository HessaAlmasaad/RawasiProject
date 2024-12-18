from django import forms
from .models import InvestmentFund

class InvestmentFundForm(forms.ModelForm):
    class Meta:
        model = InvestmentFund
        fields = ['name', 'description', 'is_active',]
        widgets = {
            'is_active': forms.Select(choices=[(True, 'نشط'), (False, 'غير نشط')]),
            'category': forms.Select(choices=[('Stocks', 'أسهم'), ('Real Estate', 'عقارات')]),
        }
