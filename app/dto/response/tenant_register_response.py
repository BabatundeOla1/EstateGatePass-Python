class TenantRegisterResponse:
    message: str

    def to_dictionary(self):
        return {
            'message': self.message
        }