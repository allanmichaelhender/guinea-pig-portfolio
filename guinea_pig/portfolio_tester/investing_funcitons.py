

def invest_daily(FTSE_weight,SNP500_weight,queryset):
    total_shares = 0
    total_invested = 0
    iShares_World_total_shares = 0
    iShares_SNP500_total_shares = 0
    Vanguard_Global_Bond_total_shares = 0
    Cash_total = 0

    for daily_entry in queryset:
        
