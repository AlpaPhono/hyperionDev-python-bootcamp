from tabulate import tabulate
#===========================================
# Example of using tabulate module 
#===========================================
data = [["Himanshu",1123,10023],["Rohit",1126,10029], ["Sha",111178,7355.4]]
print(tabulate(data, headers=["Name","User ID","Roll. No. "]))

#===========================================
# Defining header along with data
#===========================================
print("Example2")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers="firstrow"))

#===========================================
# Displaying Indicies of the rows using the show index parameter
#===========================================
print("Example 3")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always"))

#=============================================
# There are different table formats 
#=============================================
print("Plain Table")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always", tablefmt="plain"))

print("Fancy Grid")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always", tablefmt="fancy_grid"))

print("Jira")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always", tablefmt="jira"))

print("HTML")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always", tablefmt="html"))

print("textile")
data = [["Name","ID"],["Himanshu",1123],["Rohit",1123],["sha",111178]]
print(tabulate(data, headers= "firstrow", showindex="always", tablefmt="textile"))

# REFERENCES
# https://analyticsindiamag.com/beginners-guide-to-tabulate-python-tool-for-creating-nicely-formatted-tables/