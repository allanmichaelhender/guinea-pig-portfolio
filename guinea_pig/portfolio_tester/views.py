from django.shortcuts import render
from .models import FtseData, Snp500Data
from .investing_funcitons import invest_daily
import datetime





def portfolio_tester_home(request):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 2, 1)
    queryset=FtseData.objects.filter(date__range=(start_date,end_date))

    total_value = invest_daily(1,start_date,end_date,FTSE_weight=1,FTSE_queryset=queryset)

    return render(request, 'portfolio_tester/portfolio_tester_home.html', {'newdata': queryset, 'total_value': total_value})