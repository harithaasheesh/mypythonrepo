fixed_amount=10000
withdraw=int(input("enter the amount to withdraw"))
if withdraw<=fixed_amount:
    balance=fixed_amount-withdraw
    print("sucess!!! your balance=",balance)
else:
    print("insuffitient amount")


# current_amount=10000
# amount=float(input("enter the amound to witdraw"))
# cracc= current_amount-amount
# if amount>current_amount:
#     print("insufficiant balance")
# else:
#     print("transaction sucessful, your current balance is",cracc)