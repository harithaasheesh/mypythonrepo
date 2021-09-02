employees=[
    {"e_id":1000,"e_name":"ram","salary":20000,"department":"testing","exp":1},
    {"e_id": 1001,"e_name":"ravi","salary": 25000,"department":"testing","exp":1},
    {"e_id": 1002,"e_name": "raj","salary": 23000,"department": "developer","exp": 1},
    {"e_id": 1003,"e_name":"nikil", "salary":28000,"department":"developer","exp": 2},
]
#print employees name
# for employee in employees:     #map
#     print(employee["e_name"])

e_names=list(map(lambda employee:employee['e_name'],employees))
print(e_names)
    #print employee names in uppercase
# for employee in employees:
#    print(employee["e_name"].upper())

e_upper=list(map(lambda emp:emp['e_name'].upper(),employees))
print(e_upper)
#print employe name working as developer

# for employee in employees:
#     if(employee["department"=="developer"]):    #filter
#         print(employee["e_name"])
developers=list(filter(lambda employee:employee['department']=='developer',employees))
print(developers)
developers_name=list(map(lambda dev:dev['e_name'],developers))
print(developers_name)
#total salaries
# total=0
# for employee in employees:       #reduce
#     total+=employee['salary']
# print(total)
salary=sum(map(lambda emp:emp['salary'],employees))
print(salary)
#maximum salary
salary=max(map(lambda emp:emp['salary'],employees))
print(salary)
#1.case map
#2.CASE FILTER
#3.CASE REDUCE

#reduce not directly available.we have to import that module

#PRINT emplyee name starying with "a" :filter
#print highest salary :reduce
#print lowest salary:reduce
#add bonus for all employees :map
#add bonus of 500rs for developers: filter