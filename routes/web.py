"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup



ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    
    RouteGroup([
        Get("/", "EmployeeController@index").name("index"),
        Get("/@id", "EmployeeController@show").name("show"),
        Post("/", "EmployeeController@create").name("create"),
        Put("/@id", "EmployeeController@update").name("update"),
        Delete("/@id", "EmployeeController@destroy").name("destroy")
    ], prefix="/employees", name="employees")
]
