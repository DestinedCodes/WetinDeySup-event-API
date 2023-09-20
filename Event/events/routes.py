# pylint: disable=cyclic-import
"""_summary_
"""
# pylint: disable=unused-import
from flask import Blueprint, request, jsonify
from Event.models import Users, Groups
from Event.utils import (
    query_one_filtered,
    query_paginate_filtered,
    query_paginated,
)

# url_prefix includes /events before all endpoints in blueprint
events = Blueprint("events", __name__, url_prefix="/api/events")


@events.route("/", methods=["POST"])
def add_provider():
    """_summary_
    """
    return


# groups = Blueprint("groups", __name__, url_prefix="/api/groups")
# @groups.route("/<string:groupId>", methods=["GET"])
# def get_group_by_id(groupId):
#     """
#     Get details of a group ny its group ID

#     Args:
#         groupId (str): The ID of the group to get

#     Returns:
#         dict: A JSON response with group details
#     """
#     try:
#         group = Groups.query.filter_by(group_id=groupId).first()
        
#         if group:
#             # Create a dictionary with group details
#             group_details = {
#                 "group_id": group.group_id,
#                 "title": group.title
#             }
#             return jsonify({
#                 "status": "success",
#                 "message":"Group details successfully fetched",
#                 "data": group_details
#             })
#         else:
#             return jsonify({
#                 "status": "failed",
#                 "message": f"Group with groupId {groupId} not found"
#             }),404
#     except Exception as e:
#         print(f'{type(e).__name__}: {e}')
#         return jsonify({
#             'status': 'failed',
#             'message': 'An error occurred while fetching group details'
#         }), 500
    