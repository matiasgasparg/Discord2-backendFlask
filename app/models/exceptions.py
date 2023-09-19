from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
class userNotFound(CustomException):
    def __init__(self, user_id):
        super().__init__(404, "User Not Found", f"User with id {user_id} not found")
class InvalidDataError(CustomException):
    def __init__(self, description):
        super().__init__(400, "Invalid Data", description)
class duplicateError(CustomException):
    def __init__(self):
        super().__init__(409, "Ya existe un usuario con el mismo username y/o contraseña")