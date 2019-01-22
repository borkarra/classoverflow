class Config(object):
    DEBUG = False
    TESTING = False

    db_username = 'baac0f77f7e8d1'
    db_password = '0c4f074b'
    db_host     = 'us-cdbr-iron-east-01.cleardb.net'
    db_db       = 'heroku_9eccdaa5e0bf49c'
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(db_username,
                                                            db_password,
                                                            db_host,
                                                            db_db)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True