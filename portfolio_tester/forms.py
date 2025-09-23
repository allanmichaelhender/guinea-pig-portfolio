from django import forms
from .models import Portfolios

frequency_choices = (('daily','Daily'), ('monthly', 'Monthly'))

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolios
        exclude = ["final_amount", "change_percentage", "total_amount_invested", "user"]
        #fields = "__all__"
        
        
        widgets = {
            'investment_frequency': forms.RadioSelect(),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'FTSE_weight': forms.NumberInput(attrs={'step': '0.01', 'class': 'weight-input'}),
            'SNP500_weight': forms.NumberInput(attrs={'step': '0.01', 'class': 'weight-input'}),
            'NIKKEI225_weight': forms.NumberInput(attrs={'step': '0.01', 'class': 'weight-input'}),
        }
        
        initial = {
            'investment_amount': 0,
            'FTSE_weight': 0,
            'SNP500_weight': 0,
            'NIKKEI225_weight': 0,
        }
