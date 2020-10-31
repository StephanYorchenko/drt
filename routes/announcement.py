from flask import request, render_template, jsonify


def render_page():
	return render_template('announcement.html', is_admin=True, is_hostes=True)


def get_announcements():
	page_number = request.args.get('page_number')
	print(page_number)
	return jsonify({
			'count': 15,
			'announcements':
				[
						{'title': 'Hello',
						 'text': 'World',
						 'date': '2020-12-20'}
				] * 10
	})
