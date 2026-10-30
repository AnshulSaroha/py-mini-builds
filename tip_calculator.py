#Tip Calculator
#calulates tip amount and share per person

#taking input from user
bill = float(input("Enter the bill amount: "))
number_of_people = int(input("Enter the number of people: "))
own_tip = input("Do you want your own tips --> (yes or no):  ")


#choosing own tip percentage
if (own_tip == "yes"):
    tip_percent = int(input("Enter the tip percentage: "))
    if (tip_percent>=0) and (tip_percent<=50):
        tip = bill*(tip_percent/100)
    else:
        print("tip should be between 0 to 50 : continue without tip")
        tip = 0
else:
#Calculating the tip
def tip_cal():    
    if(bill>=5000):
        print("bill is 5000 or more --> applying 0% tip")
        tip = 0
    elif(bill>=500):
        print("bill is 500 or more --> applying 5% tip")
        tip = bill*0.05 
    else:
        print("bill is under 500 --> applying 10% tip")
        tip=bill*0.1

#calculating total bill
bill+= tip

#calculating share per person
share = round((bill/number_of_people),2)

#printing final output
print()
print(f"The Total bill with the tip is: {bill}")
print(f"Share per person is: {share}")