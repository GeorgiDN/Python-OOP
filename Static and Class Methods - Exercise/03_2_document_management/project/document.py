from project.topic import Topic
from project.category import Category

class Document:
    def __init__(self, _id: int, category_id: int, topic_id: int, file_name: str):
        self.id = _id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: list = []

    @classmethod
    def from_instances(cls, _id: int, category: Category, topic: Topic, file_name: str):
        return cls(_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        tag = self._find_tag(tag_content)
        if not tag:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        tag = self._find_tag(tag_content)
        if tag:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        return (f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, "
                f"tags: {', '.join(self.tags)}")

    def _find_tag(self, tag_content):
        return tag_content in self.tags
