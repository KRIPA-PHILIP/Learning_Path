class SessionMemory:

    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id):

        if session_id not in self.sessions:

            self.sessions[session_id] = {
                "learning_path": "",
                "chat_history": []
            }

    def save_learning_path(self, session_id, learning_path):

        self.create_session(session_id)

        self.sessions[session_id]["learning_path"] = learning_path

    def get_learning_path(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["learning_path"]

    def add_chat(self, session_id, role, content):

        self.create_session(session_id)

        self.sessions[session_id]["chat_history"].append(
            {
                "role": role,
                "content": content
            }
        )

    def get_chat_history(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["chat_history"]


memory = SessionMemory()