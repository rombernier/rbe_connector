from rbe_connector_modules import Rbe_ConnectorModule
from rbe_connector_modules.connector import RBEConnector

if __name__ == "__main__":
    module = Rbe_ConnectorModule()
    module.register(RBEConnector, "RBEConnector")
    module.run()
