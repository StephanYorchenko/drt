from flask import jsonify, make_response, redirect, request
from infrastructure import DBUser


def check_auth():
    username = request.args.get('name')
    user_hash = request.args.get('password')

    result = DBUser.check_user(username, user_hash)

    return jsonify({"result": result})


def try_authorize():
    username = request.form.get('name')
    user_hash = request.form.get('password')

    user = DBUser.get_user(name=username)

    role_to_int = {
        'employee': 0,
        'admin': 1,
        'hostess': 2
    }

    name = user.name if user is not None else ''
    role = str(user.role) if user is not None else ''

    resp = make_response(
        jsonify({
            "authorized": bool(user) and user.user_hash == user_hash,
            'Name': name,
            'Role': role
        })
    )

    resp.set_cookie('name', name)
    resp.set_cookie('role', role)

    return resp


def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('role', '', expires=0)
    return resp
