# -*- coding: UTF-8 -*-
from ..interfaces import ICollectiveBehaviorSeoSettings
from collective.behavior.seo import _
from plone.app.registry.browser import controlpanel


class CollectiveBehaviorSeoSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICollectiveBehaviorSeoSettings
    label = _(u'Collective Behavior SEO settings')

    def updateFields(self):
        super(CollectiveBehaviorSeoSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(CollectiveBehaviorSeoSettingsEditForm, self).updateWidgets()


class CollectiveBehaviorSeoSettingsControlPanel(
        controlpanel.ControlPanelFormWrapper):
    form = CollectiveBehaviorSeoSettingsEditForm
