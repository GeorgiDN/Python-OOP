from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for page, photo in enumerate(self.photos):
            if len(photo) < 4:
                photo.append(label)
                slot = photo.index(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot + 1}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = [separator]
        for page in self.photos:
            result.append(' '.join("[]" for _ in page))
            result.append(separator)
        return "\n".join(result)


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



###################################################################################################
# from math import ceil
# 
# 
# class PhotoAlbum:
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = [[] for _ in range(self.pages)]
# 
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         return cls(ceil(photos_count / 4))
# 
#     def add_photo(self, label: str):
#         for num, page in enumerate(self.photos):
#             if len(page) < 4:
#                 page.append(label)
#                 return f"{label} photo added successfully on page {num + 1} slot {len(page)}"
#         return "No more free slots"
# 
#     def display(self):
#         separator = '-' * 11 + "\n"
#         result = separator
#         for page in self.photos:
#             result += " ".join(["[]" for _ in page]) + "\n"
#             result += separator
#         return result.strip()



####################################################################################################
# from math import ceil
#
#
# class PhotoAlbum:
#     PAGE_CAPACITY = 4
#
#     def __init__(self, pages: int):
#         self.pages = pages
#         self.photos = [[]for _ in range(pages)]
#
#     @classmethod
#     def from_photos_count(cls, photos_count: int):
#         return cls(ceil(photos_count / cls.PAGE_CAPACITY))
#
#     def add_photo(self, label: str):
#         for idx in range(len(self.photos)):
#             if len(self.photos[idx]) < PhotoAlbum.PAGE_CAPACITY:
#                 self.photos[idx].append(label)
#                 return f"{label} photo added successfully on page {idx + 1} slot {len(self.photos[idx])}"
#         return "No more free slots"
#
#     def display(self):
#         result = ["-----------"]
#         for row in self.photos:
#             if row:
#                 line = ["[]" for _ in range(len(row))]
#                 result.append(f"{' '.join(line)}\n-----------")
#             else:
#                 result.append("\n-----------")
#
#         return '\n'.join(result)
