from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    a = Appearance(rating=data["rating"], guest_id=data["guest_id"], episode_id=data["episode_id"])
    db.session.add(a)
    db.session.commit()
    return jsonify({"id": a.id, "rating": a.rating}), 201
