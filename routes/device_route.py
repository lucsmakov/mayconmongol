from flask import Blueprint, request, jsonify
from services.device_service import *
from utils.error_messages import ERRO
devices_bp = Blueprint('devices', __name__, url_prefix='')
@devices_bp.route('/devices', methods=['POST'])
def create():
    info_body = request.json
    new_device, erro = create_device(info_body)
    if erro:
        erro_info = ERRO.get(erro, {'message': 'Unknown error', 'status_code': 500})
        return jsonify({'message': erro_info['message']}), erro_info['status_code']
    return jsonify(new_device.to_dict()), 201

@devices_bp.route('/devices', methods=['GET'])
def list_devices():
    return jsonify(device_list()), 200

@devices_bp.route('/devices/<int:id>', methods=['GET'])
def chosen_device(id):
    device_found = chosen_device_list(id)
    return jsonify(device_found), 200

@devices_bp.route('/devices/<int:id>', methods=['PATCH', 'PUT'])
def update(id):
    device = update_device(id, request.json)
    return jsonify(device.to_dict()), 200

@devices_bp.route('/devices/<int:id>', methods=['DELETE'])
def delete(id):
    result = delete_device(id)
    if result:
        return "", 204