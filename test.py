lower_bound = 10
width = 10
quantity = 48
for low in range(lower_bound, lower_bound + quantity * width + 1, width):
    print (', (6,' '''distanceG2,''',int(low/10),',[',low, '-', low+width,'),', low,',',low+width,')')
