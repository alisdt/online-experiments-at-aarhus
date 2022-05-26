
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = 'A simple demo passing on information delivered via paced word-at-a-time reading.'
class Constants(BaseConstants):
    name_in_url = 'telephone'
    players_per_group = 3
    num_rounds = 3
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    response = models.StringField()