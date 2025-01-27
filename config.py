class Config(object):
    DEBUG=False
    TESTING = False

    SECRET_KEY ='a9yf19205345fcf10d49'
    SMTP_PORT = 586
    SMTP_SERVER = "smtp.gmail.com"
    EMAIL_FROM = 'fircutt@gmail.com'
    # EMAIL_LIST = '99293@yandex.tj'
    EMAIL_LIST = 'pazj@mail.ru'
    # PSWD = "saffir" # Original password
    PSWD = 'yhpg gkvc butv pgnq'
    
    SESSION_COOKIE_SECURE =True

    UPLOAD_FOLDER = 'static/temp_save'
    REFRESH_DATA = 'data'

    USR = 'minfir'
    PSW = 'fir2024_$'

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