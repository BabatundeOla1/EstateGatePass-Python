from dataclasses import dataclass


@dataclass
class TenantLoginRequest:

    email: str
    password: str

    def to_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }
