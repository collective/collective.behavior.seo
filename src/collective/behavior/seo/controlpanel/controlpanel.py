# -*- coding: UTF-8 -*-
from plone.app.registry.browser import controlpanel
from collective.behavior.seo import _
from ..interfaces import ICollectiveBehaviorSeoSettings


class CollectiveBehaviorSeoSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICollectiveBehaviorSeoSettings
    label = _(u'Collective Behavior SEO settings')
    description = _(u'')

    def updateFields(self):
        super(CollectiveBehaviorSeoSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(CollectiveBehaviorSeoSettingsEditForm, self).updateWidgets()


class CollectiveBehaviorSeoSettingsControlPanel(
        controlpanel.ControlPanelFormWrapper):
    form = CollectiveBehaviorSeoSettingsEditForm
