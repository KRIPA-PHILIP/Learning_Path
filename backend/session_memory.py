class SessionMemory:

    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id):

        if session_id not in self.sessions:

            self.sessions[session_id] = {

                # Resume Pipeline
                "resume_text": "",

                "candidate_profile": {},

                "recommended_careers": [],

                "selected_career": "",

                "skill_gap": {},

                # Existing Learning Path
                "learning_path": "",

                # Existing Chat
                "chat_history": []

            }

    # -------------------------
    # Resume
    # -------------------------

    def save_resume(self, session_id, resume_text):

        self.create_session(session_id)

        self.sessions[session_id]["resume_text"] = resume_text

    def get_resume(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["resume_text"]

    # -------------------------
    # Candidate Profile
    # -------------------------

    def save_candidate_profile(self, session_id, profile):

        self.create_session(session_id)

        self.sessions[session_id]["candidate_profile"] = profile

    def get_candidate_profile(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["candidate_profile"]

    # -------------------------
    # Career Recommendation
    # -------------------------

    def save_recommended_careers(self, session_id, careers):

        self.create_session(session_id)

        self.sessions[session_id]["recommended_careers"] = careers

    def get_recommended_careers(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["recommended_careers"]

    # -------------------------
    # Selected Career
    # -------------------------

    def save_selected_career(self, session_id, career):

        self.create_session(session_id)

        self.sessions[session_id]["selected_career"] = career

    def get_selected_career(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["selected_career"]

    # -------------------------
    # Skill Gap
    # -------------------------

    def save_skill_gap(self, session_id, skill_gap):

        self.create_session(session_id)

        self.sessions[session_id]["skill_gap"] = skill_gap

    def get_skill_gap(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["skill_gap"]

    # -------------------------
    # Existing Learning Path
    # -------------------------

    def save_learning_path(self, session_id, learning_path):

        self.create_session(session_id)

        self.sessions[session_id]["learning_path"] = learning_path

    def get_learning_path(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["learning_path"]

    # -------------------------
    # Existing Chat History
    # -------------------------

    def add_chat(self, session_id, role, content):

        self.create_session(session_id)

        self.sessions[session_id]["chat_history"].append({

            "role": role,

            "content": content

        })

    def get_chat_history(self, session_id):

        self.create_session(session_id)

        return self.sessions[session_id]["chat_history"]


memory = SessionMemory()