import os


class SystemConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4'.format(
    **{
        'user': os.getenv('DB_USER', 'mysql'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('MYSQL_PORT', '3306'),
        'database': os.getenv('DB_DATABASE', 'mysql')
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
Config = SystemConfig