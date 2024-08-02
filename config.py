class Config(object):
    DEBUG=False
    TESTING = False

    SECRET_KEY ='a9yf82b33072234619205345fcf10d49'
    SMTP_PORT = 587
    SMTP_SERVER = "smtp.gmail.com"
    EMAIL_FROM = 'saffircutton@gmail.com'
    # EMAIL_LIST = '992934446668@yandex.tj'
    EMAIL_LIST = 'parvizjan@inbox.ru'
    # PSWD = "saffircutton_$" # Original password
    PSWD = 'yhpg gkvc butv pgnq'
    
    SESSION_COOKIE_SECURE =True

    UPLOAD_FOLDER = 'static/temp_save'
    REFRESH_DATA = 'data'

    USR = 'adminSaffir'
    PSW = 'Saffir2024_$'

    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

class ProductionConfig(Config):
    ...
class DevelopmentConfig(Config):
    DEBUG=True

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING=True
    SESSION_COOKIE_SECURE = False