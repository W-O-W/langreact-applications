from langreact.core.configure.default import Configure
from langreact.core.application import Application, OpenAISession, Session
from langreact.core.plugin.plugins import ApplicationPlugin


class OpenaiChatApplication(Application):
    def __init__(self, configure: Configure) -> None:
        super().__init__(configure)

    def new_session(self, context, system_context_text="") -> Session:
        session = OpenAISession()
        if system_context_text != "":
            session.add_message(system_context_text, role="system")


class OpenaiChatApplicationPlugin(ApplicationPlugin):
    def __init__(self):
        super().__init__("openai_chat", "0.1")

    def create_new_application(
        self, local_context, configure, reflection=False
    ) -> Application:
        return OpenaiChatApplication(configure)
