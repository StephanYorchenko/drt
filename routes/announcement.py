from flask import request


def get_announcements():
    page_number = request.args.get('page_number')

    return None
