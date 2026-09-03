from pydantic import BaseModel, Field


class Rbe_ConnectorModuleConfiguration(BaseModel):
    api_key: str = Field(..., description="API Key", secret=True)
    api_base_url: str = Field(..., description="API Base URL", secret=True)
