import datetime

def invest_daily(amount_daily, start_date, end_date, FTSE_weight=0, SNP500_weight=0, FTSE_queryset=None, SNP500_queryset=None):
    total_shares = 0
    total_invested = 0
    iShares_World_total_shares = 0
    iShares_SNP500_total_shares = 0
    Vanguard_Global_Bond_total_shares = 0
    Cash_total = 0
    value=0

    timeframe = end_date - start_date
    total_days = timeframe.days 
    total_amount_to_invest = total_days*amount_daily
    
    aggregated_amount_per_day = total_amount_to_invest/(len(FTSE_queryset)+1)
    

    print(aggregated_amount_per_day)

    for daily_entry in FTSE_queryset:
        pass
        total_shares += (aggregated_amount_per_day/float(daily_entry.close))*FTSE_weight
        value = total_shares*float(daily_entry.close)

    return round(value,2)


