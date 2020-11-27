from flask import render_template


def main():
	return render_template('main.html', is_admin=True, is_hostes=False)
