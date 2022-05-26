
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.swap_players()
class DescribeImage(Page):
    form_model = 'group'
    form_fields = ['description']
    timeout_seconds = 15
    def is_displayed(self):
        return self.player.id_in_group == 1
    def error_message(self, values):
        if len(values["description"]) > 20:
            return "Message too long!"
class P2Wait(WaitPage):
    pass
class SelectDescribedImage(Page):
    form_model = 'group'
    form_fields = ['image_selected']
    def is_displayed(self):
        return self.player.id_in_group == 2
page_sequence = [ShuffleWaitPage, DescribeImage, P2Wait, SelectDescribedImage]