def calculate_bill(price, quantity) :
    totalbill=price*quantity
    if(totalbill>2000):
        discount = totalbill * (10/100)
        totalbill = totalbill - discount
    return totalbill
  
result=calculate_bill(500,5)
print("The Total Bill is :",result)
    
    