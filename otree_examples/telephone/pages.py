
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Debug1(Page):
    form_model = 'player'
    def vars_for_template(self):
        if "last_response" in self.session.vars:
            return { "last_response": self.session.vars["last_response"] }
        else:
            return { "last_response": "Not yet!" }
class Reading(Page):
    form_model = 'player'
    def is_displayed(self):
        # only show this for player 1 in round 1, etc.
        return self.player.id_in_group == self.subsession.round_number
    def vars_for_template(self):
        if "last_response" in self.session.vars:
            # there is a response from the last round, return this
            return { "last_response": self.session.vars["last_response"] }
        else:
            # there isn't, fill in
            return { "last_response": "This is an example text to remember and type out" }
class Writing(Page):
    form_model = 'player'
    form_fields = ['response']
    def is_displayed(self):
        # only show this for player 1 in round 1, etc.
        return self.player.id_in_group == self.subsession.round_number
    def before_next_page(self):
        self.session.vars["last_response"] = self.player.response
class WaitFinishedReading(WaitPage):
    pass
page_sequence = [Debug1, Reading, Writing, WaitFinishedReading]