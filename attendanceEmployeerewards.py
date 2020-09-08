import operator
def readEmployeedetails ():
 print ("enter the number of employees":)
 numberofEmployees=int(input())
 employeeRecord={}
 for employee in range (0, numberofEmployees):
  print ("enter employee name:")
  name=input ()
  print (" enter attendance of employee")
  attendance=int(input())
  employeeRecord [name]=attendance
  print ()
  return employeeRecord

def rankEmployees (employeeRecord):
 sortedEmployeeRecord=sorted (employeeRecord.items())
 print(sortedEmployeeRecord)
 print ("{} has secured first rank, scoring {} attendance".format(sortedEmployeeRecord [0][0], sortedEmployeeRecord [0][1])
 print ("{} has secured second rank, scoring {} attendance".format(sortedEmployeeRecord [1][0], sortedEmployeeRecord [1][1])
 print ("{} has secured third rank, scoring {} attendance".format(sortedEmployeeRecord [2][0], sortedEmployeeRecord [2][1])
 key=operator.itemgetter(1)
 reverse=True
 print()

def rewardEmployees(sortedEmployeeRecord, reward):
 print("{}has received a cash reward of${}".format(sortedEmployeeRecord [0][0], reward [0]))
 print("{}has received a cash reward of${}".format(sortedEmployeeRecord [1][0], reward [1]))
 print("{}has received a cash reward of${}".format(sortedEmployeeRecord [2][0], reward [2]))
 print()
