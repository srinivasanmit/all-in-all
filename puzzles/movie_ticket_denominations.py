def check_ticket_price_denominations(price_list) :
    opening_bal = 0
    for deno in price_list :
        if deno - 25 <= opening_bal :
            opening_bal += 25
        else :
            return False
    return True

print [25,25,50,100,50]
print check_ticket_price_denominations([25,25,50,100,50])
print [25,50,100]
print check_ticket_price_denominations([25,50,100])
