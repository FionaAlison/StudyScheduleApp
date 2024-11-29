import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://fiona:fiona@database-service:5432/studyapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

