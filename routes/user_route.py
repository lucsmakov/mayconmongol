from flask import Blueprint, request, jsonify
from services.user_service import *
from utils.error_messages import ERROR as ERRO

users_bp = Blueprint('users', __name__, url_prefix='')
# //
@users_bp.route('/users',methods=['POST'])
def create():
    info_body = request.json
    new_user, erro = create_user(info_body)
    print(new_user)
    if erro:
        erro_info = ERRO.get(erro, {'message': 'Unknown error', 'status_code': 500})
        return jsonify({'message': erro_info['message']}), erro_info['status_code']
    return jsonify(new_user.to_dict()), 201

@users_bp.route('/users', methods=['GET'])
def list_users():
    return jsonify(user_list()), 200

@users_bp.route('/users/<int:id>', methods=['GET'])
def chosen_user(id):
    user_found, erro = chosen_user_list(id)
    if erro:
        erro_info = ERRO.get(erro, {'message': 'Unknown error', 'status_code': 500})
        return jsonify({'message': erro_info['message']}), erro_info['status_code']
    return jsonify(user_found.to_dict()), 200


@users_bp.route('/users/<int:id>', methods=['PATCH','PUT'])
def update(id):
    user, erro = update_user(id, request.json)
    print(erro)
    if erro:
        erro_info = ERRO.get(erro, {'message': 'Unknown error', 'status_code': 500})
        return jsonify({'message': erro_info['message']}), erro_info['status_code']
    return jsonify(user.to_dict()), 200

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete(id):
    result, erro = delete_user(id)
    if erro:
        erro_info = ERRO.get(erro, {'message': 'Unknown error', 'status_code': 500})
        return jsonify({'message': erro_info['message']}), erro_info['status_code']
    return "", 204
# //