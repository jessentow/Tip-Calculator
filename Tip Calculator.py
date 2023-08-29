charge_of_food = input("Please enter the charge of food : $ ")
print()


x = float(charge_of_food)

print("INPUT")

print()
print("Charge of Food is = $"+str(x))
print()
y= 18/100
r = float(x)
z = y*r

print("OUTPUT")  
print()
e = round(z, 2)


print ("Tips = $" +str(e))
print()

a = 7/100
b = a*r
s= round(b, 2)
print("Sales Tax = $"+str (s))

print()

k = s+e+r
print("Grand Total = $"+str(k))