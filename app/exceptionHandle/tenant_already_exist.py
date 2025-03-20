class TenantAlreadyExistsException(Exception):
    def __init__(self, message="Tenant with the given identifier already exists."):
        super().__init__(message)