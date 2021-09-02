dic={'name':'haritha','age':27,'location':'vaikom'}
def keypresent(x):
    if x in dic:
        print(x,'is present')
    else:
        print(x,'is not present')
x=input("enter key")
keypresent(x)