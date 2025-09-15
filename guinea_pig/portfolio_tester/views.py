from django.shortcuts import render
from .models import FtseData, Snp500Data
import datetime





def portfolio_tester_home(request):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 2, 2)
    queryset=FtseData.objects.filter(date__range=(start_date,end_date))






    
    return render(request, 'portfolio_tester/portfolio_tester_home.html', {'newdata': queryset})