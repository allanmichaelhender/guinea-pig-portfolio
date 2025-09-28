from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import FtseData, Snp500Data, Nikkei225Data, Portfolios
from .investing_funcitons import invest_daily, invest_monthly, test
import datetime
from .forms import PortfolioForm
from django.db.models import F, Window
from django.db.models.functions import RowNumber, ExtractYear, ExtractMonth


def portfolio_creator(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            return redirect("portfolio_tester:tester",preserve_request=True)
    else:
        form = PortfolioForm()

    return render(request, 'portfolio_tester/portfolio_tester_form.html', {'form': form})

def tester(request):
    form = PortfolioForm(request.POST)
    if form.is_valid():
        PortfolioObject = form.save(commit=False)
        if request.user.is_authenticated:
            PortfolioObject.user = request.user
        else: 
            User = get_user_model()
            PortfolioObject.user = User.objects.get(pk=2)
        
        investment_amount = PortfolioObject.investment_amount
        start_date = PortfolioObject.start_date
        end_date = PortfolioObject.end_date


        if PortfolioObject.investment_frequency == 'daily':
            FTSE_queryset=FtseData.objects.filter(date__range=(start_date,end_date)).order_by('date')
            SNP500_queryset=Snp500Data.objects.filter(date__range=(start_date,end_date)).order_by('date')
            NIKKEI225_queryset=Nikkei225Data.objects.filter(date__range=(start_date,end_date)).order_by('date')

            FTSE_weight = PortfolioObject.FTSE_weight
            SNP500_weight = PortfolioObject.SNP500_weight
            NIKKEI_weight = PortfolioObject.NIKKEI225_weight


            return_array = invest_daily(investment_amount,
                                        start_date,
                                        end_date,
                                        FTSE_weight,
                                        SNP500_weight,
                                        NIKKEI_weight,
                                        FTSE_queryset,
                                        SNP500_queryset,
                                        NIKKEI225_queryset)

            print("test")
            PortfolioObject.total_amount_invested = return_array[0]
            PortfolioObject.final_amount = return_array[4]
            change_percentage = (return_array[4]*100/float(return_array[0]))
            PortfolioObject.change_percentage = change_percentage - 100
            PortfolioObject.save()

            return redirect('portfolio_tester:my_portfolios')
        

        elif PortfolioObject.investment_frequency == 'monthly':
            FTSE_monthly_queryset = FtseData.objects.annotate(
            row_number=Window(
            expression=RowNumber(),
            partition_by=[ExtractYear('date'), ExtractMonth('date')],
            order_by=F('date').asc(),)).filter(row_number=1)

            FTSE_monthly_queryset = FTSE_monthly_queryset.filter(date__range=(start_date,end_date)).order_by('date')

            SNP500_monthly_queryset = Snp500Data.objects.annotate(
            row_number=Window(
            expression=RowNumber(),
            partition_by=[ExtractYear('date'), ExtractMonth('date')],
            order_by=F('date').asc(),)).filter(row_number=1)

            SNP500_monthly_queryset = SNP500_monthly_queryset.filter(date__range=(start_date,end_date)).order_by('date')

            NIKKEI225_monthly_queryset = Nikkei225Data.objects.annotate(
            row_number=Window(
            expression=RowNumber(),
            partition_by=[ExtractYear('date'), ExtractMonth('date')],
            order_by=F('date').asc(),)).filter(row_number=1)

            NIKKEI225_monthly_queryset = NIKKEI225_monthly_queryset.filter(date__range=(start_date,end_date)).order_by('date')

            FTSE_weight = PortfolioObject.FTSE_weight
            SNP500_weight = PortfolioObject.SNP500_weight
            NIKKEI_weight = PortfolioObject.NIKKEI225_weight


            return_array = invest_monthly(investment_amount,
                                        start_date,
                                        end_date,
                                        FTSE_weight,
                                        SNP500_weight,
                                        NIKKEI_weight,
                                        FTSE_monthly_queryset,
                                        SNP500_monthly_queryset,
                                        NIKKEI225_monthly_queryset)

            PortfolioObject.total_amount_invested = return_array[0]
            PortfolioObject.final_amount = return_array[4]
            change_percentage = (return_array[4]*100/float(return_array[0]))
            PortfolioObject.change_percentage = change_percentage - 100
            PortfolioObject.save()

            return redirect('portfolio_tester:my_portfolios')


def my_portfolios(request):
    if request.user.is_authenticated:
        portfolios = Portfolios.objects.filter(user=request.user).order_by('id')
    else: 
        User = get_user_model()
        portfolios = Portfolios.objects.filter(user=User.objects.get(pk=2)).order_by('id')
    return render(request, 'portfolio_tester/my_portfolios.html', {'portfolios': portfolios})