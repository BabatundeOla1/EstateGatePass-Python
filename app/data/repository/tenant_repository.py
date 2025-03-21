from flask_pymongo import PyMongo


class TenantRepository:
    def __init__(self, mongo: PyMongo):
        self.mongo = mongo

    def save_tenant(self, tenant):
        tenant_data = self.mongo.db.tenant.insert_one(tenant.to_dictionary())
        return tenant_data

    def find_tenant_by_name(self, name: str):
        tenant_data = self.mongo.db.tenant.find_one({"name": name})
        return tenant_data

    def find_tenant_by_email(self, email: str):
        tenant_data = self.mongo.db.tenant.find_one({"email": email})
        return tenant_data
    def delete_tenant(self, tenant):
        return self.mongo.db.tenant.delete_one(tenant)

    def get_tenant_count_from_repository(self):
        return self.mongo.db.tenant.count_documents({ })

    def clear(self):
        return self.mongo.db.tenant.delete_many({ })