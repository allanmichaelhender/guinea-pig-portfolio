from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import FtseData, Snp500Data, Nikkei225Data, Portfolios
from .investing_funcitons import invest_daily
import datetime
from .forms import PortfolioForm




def portfolio_tester_home(request):
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2025, 1, 1)
    FTSE_queryset=FtseData.objects.filter(date__range=(start_date,end_date)).order_by('date')
    SNP500_queryset=Snp500Data.objects.filter(date__range=(start_date,end_date)).order_by('date')
    NIKKEI225_queryset=Nikkei225Data.objects.filter(date__range=(start_date,end_date)).order_by('date')

    return_array = invest_daily(1,start_date,end_date,FTSE_weight=0.3,FTSE_queryset=FTSE_queryset,SNP500_weight=0.3,SNP500_queryset=SNP500_queryset,NIKKEI225_weight=0.4,NIKKEI225_queryset=NIKKEI225_queryset)

    return render(request, 'portfolio_tester/portfolio_tester_home.html', {'return_array': return_array})

def portfolio_creator(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        print("trying")
        if form.is_valid():
            print("fwaefaw")
            return redirect("portfolio_tester:tester",preserve_request=True)
    else:
        form = PortfolioForm()

    return render(request, 'portfolio_tester/portfolio_tester_form.html', {'form': form})

def tester(request):
    form = PortfolioForm(request.POST)
    if form.is_valid():
        print("here")
        PorfolioObject = form.save(commit=False)
        if request.user.is_authenticated:
            PorfolioObject.user = request.user
        else: 
            User = get_user_model()
            PorfolioObject.user = User.objects.get(pk=2)
        PorfolioObject.save()
        return render(request, 'portfolio_tester/portfolio_tester_home.html')
    
def my_portfolios(request):
    if request.user.is_authenticated:
        portfolios = Portfolios.objects.filter(user=request.user).order_by('id')
    else: 
        User = get_user_model()
        portfolios = Portfolios.objects.filter(user=User.objects.get(pk=2)).order_by('id')
    return render(request, 'portfolio_tester/my_portfolios.html', {'portfolios': portfolios})