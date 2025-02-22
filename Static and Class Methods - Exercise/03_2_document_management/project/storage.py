from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self._find_object_by_id(self.categories, category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self._find_object_by_id(self.topics, topic_id)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self._find_object_by_id(self.documents, document_id)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self._find_object_by_id(self.categories, category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self._find_object_by_id(self.topics, topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self._find_object_by_id(self.documents, document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self._find_object_by_id(self.documents, document_id)
        if document:
            return document

    def __repr__(self):
        documents = '\n'.join(map(str, [c.__repr__() for c in self.documents]))
        return documents

    @staticmethod
    def _find_object_by_id(lst, _id):
        found_object = next((obj for obj in lst if obj.id == _id), None)
        return found_object



