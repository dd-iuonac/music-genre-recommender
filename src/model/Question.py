class Question:
    def __init__(self):
        self.text = ""
        self.options = []
        self.category = ""

    @classmethod
    def from_json(cls, data):
        q = cls()
        q.__dict__ = data
        return q