
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    image_selected = models.StringField(choices=[['1', '1'], ['2', '2'], ['3', '3']])
class Player(BasePlayer):
    age = models.StringField()
    language = models.StringField()