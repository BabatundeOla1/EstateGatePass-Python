from dataclasses import dataclass


@dataclass
class Tenant:
    name: str
    room_id: str
    email: str
    password: str


    def to_dictionary(self):
        return{
            'name': self.name,
            'room_id': self.room_id,
            'email': self.email
            # 'password': self.password
        }
    @staticmethod
    def from_dictionary(data: dict):
        return Tenant(
            name=data['name'],
            room_id=data['room_id'],
            email=data['email'],
            password=data['password']
        )

