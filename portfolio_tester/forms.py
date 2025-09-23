from .models import Portfolios
import datetime
from django import forms
from django.core.exceptions import ValidationError

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

        def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")

            min_date = datetime.date(2020, 1, 1)
            max_date = datetime.date(2025, 9, 1)

            # First, check if both dates are present in the form data
            if start_date and end_date:
                # Check if the start date is before the end date
                if start_date > end_date:
                    # Add an error to the form, but not to a specific field.
                    # It will show up in `form.non_field_errors`.
                    raise ValidationError("Start date cannot be after end date.")
                
                # Check if both dates are within the required range
                if not (min_date <= start_date <= max_date and min_date <= end_date <= max_date):
                    raise ValidationError(
                        f"Dates must be between {min_date.strftime('%Y-%m-%d')} and {max_date.strftime('%Y-%m-%d')}."
                    )

            return cleaned_data
