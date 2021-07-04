# AGPL-3.0 License Copyright (c) 2021 Aditya Patil

from enum import Enum


class InputMode(Enum):
    VOICE = 'voice'
    TEXT = 'text'


class MongoCollections(Enum):
    GENERAL_SETTINGS = 'general_settings'
    CONTROL_SKILLS = 'control_skills'
    ENABLED_BASIC_SKILLS = 'enabled_basic_skills'
