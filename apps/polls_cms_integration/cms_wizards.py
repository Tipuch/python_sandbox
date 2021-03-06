from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from apps.polls_cms_integration.forms import PollWizardForm
from polls.models import Poll


class PollWizard(Wizard):
    pass

poll_wizard = PollWizard(
    title="Poll",
    weight=200,
    form=PollWizardForm,
    description="Create a new Poll",
)

wizard_pool.register(poll_wizard)
