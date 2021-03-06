from secrets import token_urlsafe

import requests
from flask import jsonify, make_response, request, Response

from application.user_manager import UserManager


class Authentication:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager

    def check_auth(self):
        username = request.form.get('name')
        user_hash = request.cookies.get('user_hash')

        result = self.user_manager.check_auth(username, user_hash)
        return jsonify({"result": result})

    def try_authorize(self):
        username = request.form.get('name')
        password = request.form.get('password')

        user = self.user_manager.get_authenticated_user(username, password)

        name = user.username if user is not None else ''
        role = user.role.value if user is not None else ''
        print()

        resp = make_response(
            jsonify({
                "authorized": bool(user) and user.password == password,
                'Name': name,
                'Role': role
            })
        )

        resp.set_cookie('name', name)
        resp.set_cookie('role', str(role))
        token = token_urlsafe(37)
        resp.set_cookie('user_hash', token)
        self.user_manager.update_user_hash(name, token)

        return resp

    @staticmethod
    def logout():
        resp = requests.request(
            method=request.method,
            url='http://localhost:8001/',
            headers={key: value
                     for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False)

        excluded_headers = ['content-encoding', 'content-length',
                            'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        response = Response(resp.content, resp.status_code, headers)
        response .set_cookie('name', '', expires=0)
        response .set_cookie('role', '', expires=0)
        response.set_cookie('user_hash', '', expires=0)
        return response
