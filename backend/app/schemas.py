from pydantic import BaseModel, validator
from humps.camel import case

from app.config import bier_settings


def to_camel(string):
    return case(string)


class Team(BaseModel):
    contact: str
    channel: str
    first_name_player_1: str
    last_name_player_1: str
    drink_pref_player_1: str
    first_name_player_2: str
    last_name_player_2: str
    drink_pref_player_2: str
    start_block: str

    @validator('start_block')
    def restrict_to_start_blocks(cls, start_block):
        if start_block not in bier_settings.start_blocks:
            raise ValueError(f'start_block must be some block: {bier_settings.start_blocks}')
        return start_block

    @validator('drink_pref_player_1')
    def restrict_to_drinks_1(cls, drink_pref_player_1):
        if drink_pref_player_1 not in bier_settings.drinks:
            raise ValueError(f'drink_pref must be one of: {bier_settings.drinks}')
        return drink_pref_player_1

    # todo: only use one validator for both
    @validator('drink_pref_player_2')
    def restrict_to_drinks_2(cls, drink_pref_player_2):
        if drink_pref_player_2 not in bier_settings.drinks:
            raise ValueError(f'drink_pref must be one of: {bier_settings.drinks}')
        return drink_pref_player_2

    @validator('channel')
    def restrict_to_channels(cls, channel):
        if channel not in ['sms', 'email']:
            raise ValueError('channel must be "sms" or "email"')
        return channel

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class Verify(BaseModel):
    to: str
    channel: str

    @validator('channel')
    def restrict_to_channels(cls, channel):
        if channel not in ['sms', 'email']:
            raise ValueError('channel must be "sms" or "email"')
        return channel

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class VerifyCheck(Verify):
    hash: str
