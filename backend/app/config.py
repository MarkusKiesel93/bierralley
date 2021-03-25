import os
from pathlib import Path
from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings, DirectoryPath


class Settings(BaseSettings):
    deploy_mode: str
    app_name: str
    frontend_domain: str

    cors_allowed_origins: list = [
        f'http://{os.getenv("FRONTEND_DOMAIN")}',
        f'https://{os.getenv("FRONTEND_DOMAIN")}',
    ]
    cors_allowed_methods: list = ['POST', 'DELETE']
    cors_allowed_headers: list = ['*']

    database: str = './db/registered.db'

    static_path: DirectoryPath = Path('./static/')

    mail_config: object = ConnectionConfig(
        MAIL_USERNAME=os.getenv('EMAIL_ADDRESS'),
        MAIL_PASSWORD=os.getenv('EMAIL_PASSWORD'),
        MAIL_FROM=os.getenv('EMAIL_ADDRESS'),
        MAIL_PORT=587,
        MAIL_SERVER='smtp.gmail.com',
        MAIL_FROM_NAME='Bierrallye Irnfritz',
        MAIL_TLS=True,
        MAIL_SSL=False,
    )

    # todo change to lower case
    TWILIO_SMS_FROM: str
    TWILIO_SID: str
    TWILIO_TOKEN: str
    TWILIO_TEST_SID: str
    TWILIO_TEST_TOKEN: str

    secret_key: str

    verify_allow_tries: int = 5
    verify_wait_minutes: int = 2

    if os.getenv('DEPLOY_MODE') == 'development':
        cors_allowed_origins: list = ['*']
        database: str = './db/dev_sqlite.db'
        secret_key: str = 'NOT_A_SECRET'


class BierrallyeSettings(BaseSettings):
    contact: str = os.getenv('EMAIL_ADDRESS')
    blocks: list = ['A', 'B', 'C', 'D', 'E', 'F']
    times: list = ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30']
    teams_per_block = 15
    drinks: list = [
      'Bier',
      'Wein + Mineral',
      'Wein + Almdudler',
      'Wein + Cola',
      'Wein + Frucade',
    ]


settings = Settings()
bier_settings = BierrallyeSettings()
