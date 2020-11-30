from flask import jsonify, make_response, redirect, request, Response
import requests

def check_auth():
	return jsonify({"result": True})


def try_authorize():
	resp = make_response(jsonify({"authorized": True,
								  'Name': 'Stephan',
								  'Role': 1}))
	resp.set_cookie('name', 'Stephan')
	resp.set_cookie('role', '1')
	return resp


def logout():
	resp = make_response(redirect('/'))
	resp.set_cookie('name', '', expires=0)
	resp.set_cookie('role', '', expires=0)

	return resp
