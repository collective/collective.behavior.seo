from ..interfaces import ICollectiveBehaviorSeoSettings
from collective.behavior.seo import _
from plone.app.registry.browser import controlpanel


class CollectiveBehaviorSeoSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICollectiveBehaviorSeoSettings
    label = _("Collective Behavior SEO settings")

    def updateFields(self):
        super().updateFields()

    def updateWidgets(self):
        super().updateWidgets()


class CollectiveBehaviorSeoSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CollectiveBehaviorSeoSettingsEditForm
