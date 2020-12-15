from flask import jsonify, request

from application.user_manager import UserManager


class UserController:
    role_to_int = {
        "EMPLOYEE": 0,
        "ADMIN": 1,
        "HOSTESS": 2
    }

    int_to_role = {
        0: "EMPLOYEE",
        1: "ADMIN",
        2: "HOSTESS"
    }

    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager

    def add_user(self):
        name = request.form.get('name')
        password = request.form.get('password')
        role = self.int_to_role[int(request.form.get('role'))]
        result = self.update_user(name, new_password=password, new_role=role)
        if not result:
            result = self.user_manager.add_user(name, password, role)

        return jsonify(
            {
                "result": result
            }
        )

    def update_user(
            self,
            current_name,
            new_name=None,
            new_password=None,
            new_role=None
    ):
        return self.user_manager.update_user(
            current_name,
            new_name,
            new_password,
            new_role
        )

    def get_user(self):
        name = request.args.get('name')

        user = self.user_manager.get_user(name)
        name = '' if user is None else user.name
        role = '' if user is None else self.role_to_int[user.role]

        return jsonify(
            {
                "name": name,
                "role": role
            }
        )

    def delete_user(self):
        name = request.form.get('username')
        self.user_manager.delete_user(name)
        return jsonify(
            {
                'result': True
            }
        )

    def get_all_users(self):
        return jsonify(
            {
                'user_list': [
                    {'name': user.name, 'role': user.role} for user in self.user_manager.get_all_users()
                ]
            }
        )
