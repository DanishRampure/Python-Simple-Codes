bill=float(input("Enter the bill amount:"))
discount=bill*0.1
total_bill=bill-discount
print(f"Discount :{discount:.2f}")
print(f"Total Amount after Discount is {total_bill}")