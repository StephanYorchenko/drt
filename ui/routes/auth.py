from flask import jsonify, make_response, redirect, request, Request
from secrets import token_urlsafe
from infrastructure import DBUser
import requests


def check_auth():
    username = request.form.get('name')
    user_hash = request.cookies.get('user_hash')

    result = DBUser.check_user(username, user_hash)
    return jsonify({"result": result})


def try_authorize():
    username = request.form.get('name')
    password = request.form.get('password')

    user = DBUser.get_user(name=username)
    name = user.name if user is not None else ''
    role = str(user.role.value) if user is not None else ''

    resp = make_response(
        jsonify({
            "authorized": bool(user) and user.password == password,
            'Name': name,
            'Role': role
        })
    )

    resp.set_cookie('name', name)
    resp.set_cookie('role', role)
    token = token_urlsafe(37)
    resp.set_cookie('user_hash', token)
    DBUser.update_user_hash(name, token)

    return resp


def logout():
    resp = requests.request(
        method=request.method,
        url='http://localhost:8002/',
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    response .set_cookie('name', '', expires=0)
    response .set_cookie('role', '', expires=0)
    response.set_cookie('user_hash', '', expires=0)
    return response
