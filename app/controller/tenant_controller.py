from flask import Flask, request, jsonify
from app.data.repository.tenant_repository import TenantRepository
from app.mapper.tenant_mapper import TenantMapper
from app.services.tenant_service import TenantServiceInterface

from app.services.tenant_services_implementation import TenantServices
from app import mongo, app

tenant_repository = TenantRepository(mongo)
tenant_service: TenantServiceInterface = TenantServices(tenant_repository)


@app.route('/register_tenant', methods=['POST'])
def register_tenant():
    data = request.get_json()

    try:
        registered_tenant = tenant_service.register_tenant(data)

        return jsonify({
            'message': 'Tenant registered successfully',
            'tenant': str(registered_tenant.inserted_id)
        }), 201

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

@app.route('/login', methods=['POST'])
def tenant_login():
    data = request.get_json()
    tenant_login_request = TenantMapper.map_to_tenant_login_request(data)

    try:
        response = tenant_service.tenant_login(tenant_login_request)
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)