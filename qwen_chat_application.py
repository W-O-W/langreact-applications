from core.application import Application, QwenLMApplication
from core.plugin.plugins import ApplicationPlugin


class QwenChatApplicationPlugin(ApplicationPlugin):
    def __init__(self):
        super().__init__("qwen_chat", "0.1")

    def create_new_application(
        self, local_context, configure, reflection=False
    ) -> Application:
        return QwenLMApplication("turbo", configure)
