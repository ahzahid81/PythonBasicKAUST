total_weight = int(input('Enter the total weight of luggage: '))
num_pieces = int(input('Number of pieces of luggage? '))

if num_pieces !=0 and total_weight/num_pieces > 50:
    print('Average weight is greater than 50 pounds -> $100 surcharge.')
    
print('Luggage check complete.')