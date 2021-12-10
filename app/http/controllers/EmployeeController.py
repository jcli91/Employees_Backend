""" A EmployeeController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Employee import Employee

class EmployeeController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request
        
    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", EmployeeController)
        """

        id = self.request.param("id")
        return Employee.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", EmployeeController)
        """

        return Employee.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", EmployeeController)
        """

        name = self.request.input("name")
        position = self.request.input("position")
        hours = self.request.input("hours")
        rate = self.request.input("rate")
        employee = Employee.create({"name": name, "position": position, "hours": hours, "rate": rate})
        return employee

    

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", EmployeeController)
        """

        name = self.request.input("name")
        position = self.request.input("position")
        hours = self.request.input("hours")
        rate = self.request.input("rate")
        id = self.request.param("id")
        Employee.where("id", id).update({"name": name, "position": position, "hours": hours, "rate": rate})
        return Employee.where("id", id).get()
    
    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", EmployeeController)
        """

        id = self.request.param("id")
        employee = Employee.where("id", id).get()
        Employee.where("id", id).delete()
        return employee