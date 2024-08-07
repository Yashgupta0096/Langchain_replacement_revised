from abc import ABC
from typing import List

from tools.base import BaseTool, BaseToolkit, ToolEnvKey, ToolEnvKeyType
from tools.zapier.zapier_send import ZapierSendTool


class ZapierSendToolkit(BaseToolkit, ABC):
    name: str = "Zapier Toolkit"
    description: str = "Toolkit containing tools for using Zapier"
    slug: str = "zapier"
    toolkit_id = "01b85de6-8d42-4596-b232-858cf35c820d"

    def get_tools(self) -> List[BaseTool]:
        return [ZapierSendTool()]

    def get_env_keys(self) -> List[ToolEnvKey]:
        return [
            ToolEnvKey(
                label="API Key",
                key="ZAPIER_NLA_API_KEY",
                key_type=ToolEnvKeyType.STRING,
                is_required=True,
                is_secret=True,
            ),
        ]
