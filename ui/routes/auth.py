from flask import jsonify, make_response, redirect, request
from infrastructure import DBUser


def check_auth():
    username = request.args.get('name')
    user_hash = request.args.get('password')

    result = DBUser.check_user(username, user_hash)

    return jsonify({"result": result})


def try_authorize():
    username = request.args.get('name')
    user_hash = request.args.get('password')

    user = DBUser.get_user(name=username)

    role_to_int = {
        'employee': 0,
        'admin': 1,
        'hostess': 2
    }

    resp = make_response(
        jsonify({
            "authorized": bool(user) and user.user_hash == user_hash,
            'Name': user.name,
            'Role': role_to_int[user.role]
        })
    )

    resp.set_cookie('name', user.name)
    resp.set_cookie('role', role_to_int[user.role])

    return resp


def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('role', '', expires=0)
    return resp
