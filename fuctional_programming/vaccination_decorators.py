def vaccination_required(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("you are not eligible for vaccination")
        else:
            return func(a,b,c)
            print("successfully completed vaccination")
    return wrapper
@vaccination_required
def vaccin(name,age,place):
    return "eligible"
print(vaccin('haritha',16,'vaikom'))