def admin_required(fucn):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("you are not allowed")
        else:
            return fucn(a,b)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_ac(user,accno):
    return str(accno)+"delete"
#print(change_pin("admin",1000))
print(delete_ac("admin",1000))