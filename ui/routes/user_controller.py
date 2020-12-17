from flask import jsonify, request

from application.user_manager import UserManager
from domain import Role


class UserController:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager

    def get_caller_name(self):
        return request.cookies.get('name')

    def add_user(self):
        name = request.form.get('name')
        password = request.form.get('password')
        role = int(request.form.get('role'))
        result = self.update_user(name, new_password=password, new_role=role)
        if not result:
            result = self.user_manager.add_user(name, password, role,
                                                self.get_caller_name())

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
            self.get_caller_name(),
            new_name,
            new_password,
            new_role
        )

    def get_user(self):
        name = request.args.get('name')

        user = self.user_manager.get_user(name)
        name = '' if user is None else user.username
        role = '' if user is None else user.role.value

        return jsonify(
            {
                "name": name,
                "role": role
            }
        )

    def delete_user(self):
        name = request.form.get('username')
        self.user_manager.delete_user(name, self.get_caller_name())
        return jsonify(
            {
                'result': True
            }
        )

    def get_all_users(self):
        return jsonify(
            {
                'user_list': [
                    {'name': user.username, 'role': user.role.value}
                    for user in self.user_manager.get_all_users(
                        self.get_caller_name())
                ]
            }
        )
