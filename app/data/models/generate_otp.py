from dataclasses import dataclass


@dataclass
class Generate_otp:
    otp_code: str
    expiration_time: str

    def to_dictionary(self):
        return {
            'otp_code': self.otp_code,
            'expiration_time': self.expiration_time
        }

    def from_dictionary(self, data: dict):
        return Generate_otp(
            otp_code= data['otp_code'],
            expiration_time= data['expiration_time']
        )

