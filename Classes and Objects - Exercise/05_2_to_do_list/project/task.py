class Task:
    def __init__(self, name:str, due_date:str):
        self.name = name
        self.due_date = due_date
        self.comments: list = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name == self.name:
            return f"Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if new_date == self.due_date:
            return f"Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if self.is_valid_index(comment_number, len(self.comments)):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"

    @staticmethod
    def is_valid_index(value, max_value):
        return 0 <= value < max_value
