from flask import Flask 
from flask import jsonify
from flask import request

app = Flask(__name__)  
EmployeeDB=[
      {
       'id':'101',
       'name':'Harry Potter',
       'salary':'1000'
       },
       { 'id':'201',
         'name':'The Davinci Code',
         'salary':'20000'
       }
]

@app.route('/employeedb/employee',methods=['GET'])
def getAllEmployees():
     return jsonify({'employees':EmployeeDB})


#get employee by ID
@app.route('/employeedb/employee/<employeeid>',methods=['GET'])
def getEmployee(employeeid):
     employee = [ em for em in EmployeeDB  if (em['id'] == employeeid) ]
     return jsonify({'em':employee})


#create new  employee
@app.route('/employeedb/employee/',methods=['POST'])
def newEmployee():
     new_employee={
       'id':request.json['id'],
       'name':request.json['name'],
       'salary':request.json['salary']
     }
      EmployeeDB .append(new_employee)
      return jsonify(new_employee)
     return jsonify({'em':employee})


  #update  employee
@app.route('/employeedb/employee/<employeeid>',methods=['PUT'])
def updateEmployee(employeeid):
     employee = [ em for em in EmployeeDB  if (em['id'] == employeeid) ]
    if 'name' in request.json:
        employee[0]['name'] = request.json['name']
    if 'salary' in request.json:
        employee[0]['salary'] = request.json['salary']
    return jsonify({'employee':employee[0]})


  @app.route('/employeedb/employee/<employeeid>',methods=['DELETE'])
def deleteBook(employeeid):
     employee = [ em for em in EmployeeDB  if (em['id'] == employeeid) ]
    if len(employee) == 0:
       abort(404)
   
    bookDB.remove(employee[0])
    return jsonify({'response':'Success'})

if __name__ == "__main__": 
    app.run()
