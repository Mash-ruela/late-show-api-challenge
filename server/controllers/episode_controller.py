from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint("episodes", __name__)

@episode_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route("/episodes/<int:id>", methods=["GET"])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    return jsonify({
        "id": e.id,
        "date": e.date,
        "number": e.number,
        "appearances": [{"id": a.id, "guest": a.guest.name, "rating": a.rating} for a in e.appearances]
    })

@episode_bp.route("/episodes/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({"message": "Deleted"})
