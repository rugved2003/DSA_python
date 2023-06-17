#Asking the user for Principal, rate of interest and time
P = float(input('Enter the principal: '))
R = float(input('Enter the rate of interest per annum: '))
T = float(input('Enter the time in years: '))
#calculating simple interest
SI = (P * R * T)/100
#caculating amount = Simple Interest + Principal
amount = SI + P
#Printing the total amount

print('Total amount:',amount)

D = float(input("Enter the discount: "))
T= amount- (SI*D)
print("discounted amount: ",T)
