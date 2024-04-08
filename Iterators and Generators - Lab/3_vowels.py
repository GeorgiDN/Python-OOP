from collections import deque


class vowels:
    VOWELS = "aeioyu"

    def __init__(self, text):
        self.vowels = deque([x for x in text if x.lower() in vowels.VOWELS])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.popleft()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

