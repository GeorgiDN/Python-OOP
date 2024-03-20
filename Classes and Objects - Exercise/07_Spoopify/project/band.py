from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        searched_album = next((a for a in self.albums if a.name == album_name),None)
        if searched_album is None:
            return f"Album {album_name} is not found."
        if searched_album.published:
            return f"Album has been published. It cannot be removed."
        self.albums.remove(searched_album)
        return f"Album {album_name} has been removed."

    def details(self):
        albums_info = "\n".join(a.details() for a in self.albums)
        result = f"Band {self.name}\n{albums_info}\n"
        return result

        # result = f"Band {self.name}\n"
        # for a in self.albums:
        #     result += f"{a.details()}\n"
        # return result


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())



####################################### TEST ############################################################
# from project.song import Song
# from project.album import Album
# from project.band import Band
#
# import unittest
#
#
# class SongTest(unittest.TestCase):
#     def test_song_init(self):
#         song = Song("A", 3.15, False)
#         message = song.get_info()
#         expected = "A - 3.15"
#         self.assertEqual(message, expected)
#
#     def test_album_init(self):
#         album = Album("The Sound of Perseverance")
#         message = album.details().strip()
#         expected = "Album The Sound of Perseverance"
#         self.assertEqual(message, expected)
#
#     def test_add_song_working(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         message = album.add_song(song)
#         expected = "Song Scavenger of Human Sorrow has been added to the album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_add_song_already_added(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.add_song(song)
#         expected = "Song is already in the album."
#         self.assertEqual(message, expected)
#
#     def test_add_song_single(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, True)
#         message = album.add_song(song)
#         expected = "Cannot add Scavenger of Human Sorrow. It's a single"
#         self.assertEqual(message, expected)
#
#     def test_add_song_published_album(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.publish()
#         message = album.add_song(song)
#         expected = "Cannot add songs. Album is published."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_working(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_not_in_album(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Song is not in the album."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_album_published(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         album.publish()
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Cannot remove songs. Album is published."
#         self.assertEqual(message, expected)
#
#     def test_publish(self):
#         album = Album("The Sound of Perseverance")
#         message = album.publish()
#         expected = album.published
#         self.assertTrue(expected)
#
#     def test_publish_message(self):
#         album = Album("The Sound of Perseverance")
#         message = album.publish()
#         expected = "Album The Sound of Perseverance has been published."
#         self.assertEqual(message, expected)
#
#     def test_details(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.details().strip()
#         expected = "Album The Sound of Perseverance\n== Scavenger of Human Sorrow - 6.56"
#
#     def test_init(self):
#         band = Band("Death")
#         message = f"{band.name} - {len(band.albums)}"
#         expected = "Death - 0"
#         self.assertEqual(message, expected)
#
#     def test_add_album_working(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         message = band.add_album(album)
#         expected = "Band Death has added their newest album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_add_album_already_added(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         band.add_album(album)
#         message = band.add_album(album)
#         expected = "Band Death already has The Sound of Perseverance in their library."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_working(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         band.add_album(album)
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album The Sound of Perseverance has been removed."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_not_found(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album The Sound of Perseverance is not found."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_published(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         album.publish()
#         band.add_album(album)
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album has been published. It cannot be removed."
#         self.assertEqual(message, expected)
#
#     def test_details(self):
#         band = Band("Death")
#         message = band.details().strip()
#         expected = "Band Death"
#         self.assertEqual(message, expected)
#
# if __name__ == '__main__':
#     unittest.main()
