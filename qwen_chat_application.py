import os
from langreact.core.application import Application, QwenLMApplication
from langreact.core.plugin.plugins import ApplicationPlugin


class QwenChatApplicationPlugin(ApplicationPlugin):
    def __init__(self):
        super().__init__("qwen_chat", "0.1")

    def create_new_application(
        self, local_context, configure, reflection=False
    ) -> Application:
        assert "DASHSCOPE_API_KEY" in os.environ, "please set DASHSCOPE_API_KEY in env"
        return QwenLMApplication("turbo", configure)
