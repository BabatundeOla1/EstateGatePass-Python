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