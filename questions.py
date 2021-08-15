from datetime import datetime

class Answer:
    def __init__(self, name: str, id: int, content: str, submittedon: datetime) -> None:
        self.name = name
        self.id = id
        self.content = content
        self.submittedon = submittedon


class Question:
    def __init__(self, query: str) -> None:
        self.query = query
        self.answers = []
    
    def add_answer(self, ans: Answer) -> None:
        self.answers.append(ans)
        self.answers.sort(key=lambda x: x.submittedon)


ans1 = Answer('Abhishek', 1, 'All sql transactions are atomic', submittedon=datetime(2021, 8, 14, 19, 28))
q1 = Question('Is updating a row in sql atomic?')
q1.add_answer(ans1)
