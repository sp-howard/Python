# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

# number of shoes
num_shoes = int(input())

# space separated list of all the shoe sizes in the shop.
# split string into list, use map function to convert each string to an integer, convert map object to a list
sizes = list(map(int, input().split(" ")))
# dictionary which containing the count of each shoe size
sizes_count = Counter(sizes)

# the number of customers
num_cust = int(input())

# total money earned
total = 0

# shoe size desired by each customer, and price of shoe
for cust in range(num_cust):
    purchase = list(map(int, input().split(" ")))
    size = purchase[0]
    price = purchase[1]
    
    if sizes_count[size] >= 1:
        total += price
        sizes_count[size] -= 1
        
print(total)    
    