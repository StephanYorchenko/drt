from flask import jsonify, make_response, redirect, request
from secrets import token_urlsafe
from infrastructure import DBUser


def check_auth():
    username = request.form.get('name')
    user_hash = request.cookies.get('user_hash')

    result = DBUser.check_user(username, user_hash)
    us = DBUser.get_user(name=username)
    print('db:', us.name, us.user_hash)
    print(username, user_hash, result)
    DBUser.update_user_hash(username, 'kek')

    return jsonify({"result": result})


def try_authorize():
    username = request.form.get('name')
    password = request.form.get('password')
    print(username, password)

    user = DBUser.get_user(name=username)
    name = user.name if user is not None else ''
    role = str(user.role.value) if user is not None else ''

    print(user.password)
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
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('role', '', expires=0)
    resp.set_cookie('user_hash', '', expires=0)
    return resp
