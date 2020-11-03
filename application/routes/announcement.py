from flask import request, render_template, jsonify
from domain.announcement.announcement_desk import AnnouncementDesk
from .get_items_from_desk import jsonify_n_serialized_objects_from_desk


def render_page():
    return render_template('announcement.html', is_admin=True, is_hostes=True)


def get_announcements():
    return jsonify_n_serialized_objects_from_desk(AnnouncementDesk(),
                                                  'announcements')
