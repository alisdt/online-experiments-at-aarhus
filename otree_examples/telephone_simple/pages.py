
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Debug1(Page):
    form_model = 'player'
class Reading1(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.player.id_in_group == 1
class Writing1(Page):
    form_model = 'player'
    form_fields = ['response']
    def is_displayed(self):
        return self.player.id_in_group == 1
class WaitFinished1(WaitPage):
    def after_all_players_arrive(self):
        self.group.next_player()
page_sequence = [Debug1, Reading1, Writing1, WaitFinished1]