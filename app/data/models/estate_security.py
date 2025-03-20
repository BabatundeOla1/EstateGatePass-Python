
class Estate_security:

    first_name: str
    last_name: str
    email: str
    password: str

    def to_dictionary(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def from_dictionary(data: dict):
        return Estate_security(
            first_name =data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = data['password']
        )
