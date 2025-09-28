import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Portfolios

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolios
        exclude = ["final_amount", "change_percentage", "total_amount_invested", "user"]
        
        widgets = {
            'investment_frequency': forms.RadioSelect(attrs={'class': 'investment-frequency-input-field'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'date-input-field'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'date-input-field'}),
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

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("Start date cannot be after end date.")
            
            min_date = datetime.date(2015, 1, 1)
            max_date = datetime.date(2025, 9, 1)
            if not (min_date <= start_date <= max_date and min_date <= end_date <= max_date):
                raise ValidationError(
                    f"Dates must be between {min_date.strftime('%Y-%m-%d')} and {max_date.strftime('%Y-%m-%d')}."
                )

        ftse_weight = cleaned_data.get("FTSE_weight")
        snp_weight = cleaned_data.get("SNP500_weight")
        nikkei_weight = cleaned_data.get("NIKKEI225_weight")

        weights = [ftse_weight, snp_weight, nikkei_weight]
        
        if all(w is not None for w in weights):
            if any(w < 0 for w in weights):
                raise ValidationError("Weights cannot be negative.")

            if not (sum(weights) == 1):
                raise ValidationError("The sum of the three weights must equal 1.")

        return cleaned_data
