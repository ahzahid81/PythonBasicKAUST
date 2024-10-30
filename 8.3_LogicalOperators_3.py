total_weight = int(input('Enter total weight of luggage:'))
num_pieces = int(input('Number of pieces of luggage?'))


if total_weight/num_pieces > 50:
    print('Average weigh is greter than 50 pounds -> $100 surchage.')
    

print('Luggage check complete.')
