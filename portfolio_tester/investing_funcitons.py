import datetime

def invest_daily(amount_daily, start_date, end_date, FTSE_weight=0, SNP500_weight=0, NIKKEI225_weight=0, FTSE_queryset=None, SNP500_queryset=None, NIKKEI225_queryset=None):

    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0

    timeframe = end_date - start_date
    total_days = timeframe.days 
    total_amount_to_invest = total_days*amount_daily
    test_invested = 0

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        FTSE_aggregated_amount_per_day = total_amount_to_invest/(len(FTSE_queryset)+1)

        for daily_entry in FTSE_queryset:
        
            FTSE_total_shares += (float(FTSE_aggregated_amount_per_day)/float(daily_entry.close))*float(FTSE_weight)

            FTSE_value = FTSE_total_shares*float(daily_entry.close)

   
    
    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        SNP500_aggregated_amount_per_day = total_amount_to_invest/(len(SNP500_queryset)+1)

        for daily_entry in SNP500_queryset:
            SNP500_total_shares += (float(SNP500_aggregated_amount_per_day)/float(daily_entry.close))*float(SNP500_weight)
            SNP500_value = SNP500_total_shares*float(daily_entry.close)
 
    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        NIKKEI225_aggregated_amount_per_day = total_amount_to_invest/(len(NIKKEI225_queryset)+1)

        for daily_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (float(NIKKEI225_aggregated_amount_per_day)/float(daily_entry.close))*float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares*float(daily_entry.close)

    

    return_array = [total_amount_to_invest, FTSE_value, SNP500_value, NIKKEI225_value, FTSE_value+SNP500_value+NIKKEI225_value]
    return return_array






def invest_monthly(amount_monthly, start_date, end_date, FTSE_weight=0, SNP500_weight=0, NIKKEI225_weight=0, FTSE_queryset=None, SNP500_queryset=None, NIKKEI225_queryset=None):

    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0

    timeframe = end_date - start_date
    total_months = timeframe.months
    total_amount_to_invest = total_months*amount_monthly
    test_invested = 0

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        FTSE_aggregated_amount_per_day = total_amount_to_invest/(len(FTSE_queryset)+1)

        for monthly_entry in FTSE_queryset:
        
            FTSE_total_shares += (float(FTSE_aggregated_amount_per_day)/float(monthly_entry.close))*float(FTSE_weight)

            FTSE_value = FTSE_total_shares*float(monthly_entry.close)

   
    
    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        SNP500_aggregated_amount_per_day = total_amount_to_invest/(len(SNP500_queryset)+1)

        for monthly_entry in SNP500_queryset:
            SNP500_total_shares += (float(SNP500_aggregated_amount_per_day)/float(monthly_entry.close))*float(SNP500_weight)
            SNP500_value = SNP500_total_shares*float(monthly_entry.close)
 
    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        NIKKEI225_aggregated_amount_per_day = total_amount_to_invest/(len(NIKKEI225_queryset)+1)

        for monthly_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (float(NIKKEI225_aggregated_amount_per_day)/float(monthly_entry.close))*float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares*float(monthly_entry.close)

    return_array = [total_amount_to_invest, FTSE_value, SNP500_value, NIKKEI225_value, FTSE_value+SNP500_value+NIKKEI225_value]
    return return_array

  


