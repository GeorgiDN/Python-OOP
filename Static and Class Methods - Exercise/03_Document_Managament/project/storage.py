from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

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
        current_category = self._find_object_by_id(self.categories, category_id)
        if current_category:
            current_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        current_topic = self._find_object_by_id(self.topics, topic_id)
        if current_topic:
            current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        current_document = self._find_object_by_id(self.documents, document_id)
        if current_document:
            current_document.edit(new_file_name)

    def delete_category(self, category_id):
        current_category = self._find_object_by_id(self.categories, category_id)
        if current_category:
            self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = self._find_object_by_id(self.topics, topic_id)
        if current_topic:
            self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = self._find_object_by_id(self.documents, document_id)
        if current_document:
            self.documents.remove(current_document)

    def get_document(self, document_id):
        current_document = self._find_object_by_id(self.documents, document_id)
        if current_document:
            return current_document

    def __repr__(self):
        return '\n'.join(map(str, self.documents))

    # Helper method
    @staticmethod
    def _find_object_by_id(lst, id_number):
        found_object = next((obj for obj in lst if obj.id == id_number), None)
        return found_object
