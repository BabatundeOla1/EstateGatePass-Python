from dataclasses import dataclass
@dataclass
class TenantRegisterRequest:
    name: str
    room_id: str
    email: str
    password: str

    def to_dictionary(self):
        return{
            'name': self.name,
            'room_id': self.room_id,
            'email': self.email,
            'password': self.password
        }