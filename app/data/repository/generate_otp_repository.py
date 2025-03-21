from datetime import datetime

from flask_pymongo import PyMongo


class GenerateOTPRepository:
    def __init__(self, mongo: PyMongo):
        self.mongo = mongo

    def save_generated_otp(self, generate_otp):
        self.mongo.db.otp_repositories.insert_one(generate_otp)

    def find_generated_otp_by_code(self, generate_otp_code: str):
        return self.mongo.db.otp_repositories.find_one({"code": generate_otp_code})

    def delete_generated_otp_by_expiration_time(self, expiration_time: datetime):
        result = self.mongo.db.otp_repositories.delete_many({"expiration_time": {"$lte": expiration_time}})
        return result.deleted_count
