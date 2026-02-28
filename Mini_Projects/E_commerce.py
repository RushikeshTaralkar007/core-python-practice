##################      MINI PROJECT 1 (User Input Version)      ########################

#####################  Smart E-Commerce Billing System   #########################



print("=== SMART BILLING SYSTEM ===")


## Take Input From User
cart_total = float(input("Enter Total Card Amount :"))
membership = input("Enter Membership (prime/normal) :").lower()
coupon_code = input("Enter Coupon Code :").upper()
payment_method = input("Enter Payment Method (UPI/ Credit Card/ Debit Card ) :").title()


discount = 0

## membership Discount 

if membership == "prime":
    discount += cart_total * 0.10

else:
    discount += cart_total * 0.05


## Coupon Logic 

valid_coupons = ["SAVE10", "SAVE20", "FESTIVE50"]

if coupon_code in valid_coupons:
    if coupon_code == "SAVE10":
        discount += cart_total * 0.10

    elif coupon_code == "SAVE20":
        discount += cart_total * 0.20

    elif coupon_code == "FESTIVE50":
        discount += cart_total * 0.50

else:
    if coupon_code != "":
        print("Invalid Coupon Applied !!!")



## Payment Method Offer 

if payment_method == "UPI":
    if cart_total >= 1000:
        discount += 100

elif payment_method == "Credit Card" or "Debit Card":
    if cart_total >=3000:
        discount += 300




## Final Calculation

final_amount = cart_total - discount


## Prevent Negative Billing 

if final_amount < 0:
    final_amount = 0

gst = final_amount * 0.18

final_bill = final_amount + gst


## Final Invoice 
print("\n==== INVOICE ====")

print("Card Total :", cart_total)
print("Total Discount :", discount)
print("GST (18%) :", gst)
print("Final Payable Amount :", final_bill)


### Thank You Notice/ Repeat Customer Service Notice

print("\n===== Thank You For Shopping =====")



        