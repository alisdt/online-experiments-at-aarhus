
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'test_example'
    players_per_group = None
    num_rounds = 2
class Subsession(BaseSubsession):
    def swap_players(self):
                if ((self.round_number % 2) == 0):
                    matrix = self.get_group_matrix()
        
                    for row in matrix:
                        row.reverse()
        
                    self.set_group_matrix(matrix)
        
class Group(BaseGroup):
    image_selected = models.StringField(choices=[['1', '1'], ['2', '2'], ['3', '3']])
    description = models.StringField()
class Player(BasePlayer):
    pass