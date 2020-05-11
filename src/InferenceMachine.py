import json

from src.model.Question import Question


class InferenceMachine:
    def __init__(self):
        self.KnowledgeBase = None
        self.Information = None
        self.Questions = None
        self.Columns = None

    def infer(self, data: dict):
        try:
            result = self.forward_chaining(self._get_choices(data))
            if "AND" in result:
                return self.find_best(self._get_choices(data))
            return result
        except Exception:
            return self.find_best(self._get_choices(data))

    def forward_chaining(self, facts_list: list):
        conclusion = facts_list[0][1]

        for fl in facts_list[1:]:
            partial_c = f"{conclusion} AND {fl[1]}"
            if partial_c in self.KnowledgeBase.keys():
                conclusion = self.KnowledgeBase[partial_c]
                if "AND" not in conclusion:
                    return conclusion
            else:
                for col in self.Columns[fl[0]]:
                    partial_c = f"{conclusion} AND {col}"
                    if partial_c in self.KnowledgeBase.keys():
                        conclusion = self.KnowledgeBase[partial_c]
                        if "AND" not in conclusion:
                            return conclusion
        return conclusion

    def find_best(self, choices: list):
        res = {}
        for k in self.Information.keys():
            res[k] = 0
        for k in self.Information.keys():
            info = self.Information[k]
            for idx, c in choices:
                if info[idx] == c:
                    res[k] += 1
        result = sorted(res, key=res.get, reverse=True)
        return result[0]

    def _get_choices(self, data: dict):
        t_key = []
        for k, v in data.items():
            t_key.append([k, self.KnowledgeBase[f"{k} = {v}"]])
        return t_key

    def get_info_description(self, genre: str):
        return self.Information[genre]["DESCRIPTION"]

    def is_ready(self):
        return self.KnowledgeBase is not None and self.Information is not None and self.Questions is not None

    def load_kb_file(self, filename: str):
        with open(filename, "r") as file:
            lines = file.readlines()

        self.KnowledgeBase = {}
        for line in lines:
            if line == "#END\n":
                break
            elif line == "\n" or "#" in line:
                continue
            else:
                split_line = line.split("THEN")
                fact = split_line[0].split("IF")[1][1:-1]
                conclusion = split_line[1][1:-1]
                self.KnowledgeBase[fact] = conclusion

    def load_questions_file(self, filename: str):
        self.Questions = []
        with open(filename, "r") as file:
            data = json.load(file)
            for _, d in data.items():
                self.Questions.append(Question.from_json(d))

    def load_info_file(self, filename: str):
        import pandas as pd
        df = pd.read_excel(filename)
        self.Information = {}
        self.Columns = {}
        for i in range(1, len(df.columns)-1):
            self.Columns[df[df.columns[i]].name] = list(set([c for c in df[df.columns[i]]]))

        self.Information = {}
        for i, g in enumerate(df[df.columns[1]]):
            self.Information[g] = {}
            for c in range(1, len(df.columns)):
                self.Information[g][df[df.columns[c]].name.replace(" ", "_")] = df[df.columns[c]][i]
