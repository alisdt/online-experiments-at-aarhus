
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class ParticipantInfo(Page):
    form_model = 'player'
    form_fields = ['age', 'language']
class ClickOnImage(Page):
    form_model = 'group'
    form_fields = ['image_selected']
page_sequence = [ParticipantInfo, ClickOnImage]