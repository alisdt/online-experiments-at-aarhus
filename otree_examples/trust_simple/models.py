
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = '\nSimple trust game\n'
class Constants(BaseConstants):
    name_in_url = 'trust_simple'
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    multiplier = 3
    instructions_template = 'trust_simple/instructions.html'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    sent_amount = models.CurrencyField(doc='Amount sent by P1', max=Constants.endowment, min=0)
    sent_back_amount = models.CurrencyField(doc='Amount sent back by P2')
    def sent_back_amount_choices(self):
        return currency_range(c(0), self.sent_amount * Constants.multiplier, c(1))
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount
class Player(BasePlayer):
    pass