from sekoia_automation.module import Module
from rbe_connector_modules.models import Rbe_ConnectorModuleConfiguration


class Rbe_ConnectorModule(Module):
    configuration: Rbe_ConnectorModuleConfiguration
