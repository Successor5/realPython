amount = int(input("enter ammount"))
years = int(input("enter number of years"))
percent = amount * 0.05
count = 0
while count<years:
 amount = amount+percent
 print(f'years{count} {amount}')
 count=count+1
