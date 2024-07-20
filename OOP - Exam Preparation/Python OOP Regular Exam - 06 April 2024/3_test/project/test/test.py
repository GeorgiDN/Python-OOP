from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia("name1", "YouTube", 10, "Information")

    def test_init(self):
        self.assertEqual(self.social_media._username, "name1")
        self.assertEqual(self.social_media._platform, "YouTube")
        self.assertEqual(self.social_media._followers, 10)
        self.assertEqual(self.social_media._content_type, "Information")
        self.assertEqual(self.social_media._posts, [])

    def test_validate_platform_with_invalid_platform(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            self.social_media._validate_and_set_platform("invalid")
        message = f"Platform should be one of {allowed_platforms}"
        self.assertEqual(message, str(ve.exception))

    def test_validate_platform_with_valid_platform_youtube(self):
        self.social_media._validate_and_set_platform("YouTube")
        self.assertEqual(self.social_media._platform, "YouTube")

    def test_validate_platform_with_valid_platform_instagram(self):
        self.social_media._validate_and_set_platform("Instagram")
        self.assertEqual(self.social_media._platform, "Instagram")

    def test_validate_platform_with_valid_platform_twitter(self):
        self.social_media._validate_and_set_platform("Twitter")
        self.assertEqual(self.social_media._platform, "Twitter")

    def test_followers_with_negative_values(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1
        message = "Followers cannot be negative."
        self.assertEqual(message, str(ve.exception))

    def test_followers_with_zero_value(self):
        self.social_media.followers = 0
        self.assertEqual(self.social_media.followers, 0)

    def test_followers_with_valid_value(self):
        self.social_media.followers = 5
        self.assertEqual(self.social_media.followers, 5)

    def test_create_post(self):
        result = self.social_media.create_post("info1")
        new_post = {'content': "info1", 'likes': 0, 'comments': []}
        message = f"New {self.social_media._content_type} post created by {self.social_media._username} on {self.social_media._platform}."
        self.assertEqual(result, message)
        self.assertEqual(self.social_media._posts, [new_post])

    def test_like_post_with_negative_index(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        result = self.social_media.like_post(-1)
        message = "Invalid post index."
        self.assertEqual(result, message)

    def test_like_post_with_index_equal_len_of_the_list(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        result = self.social_media.like_post(2)
        message = "Invalid post index."
        self.assertEqual(result, message)

    def test_like_post_with_index_greater_len_of_the_list(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        result = self.social_media.like_post(3)
        message = "Invalid post index."
        self.assertEqual(result, message)

    def test_like_post_with_valid_index(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        result = self.social_media.like_post(0)
        message = f"Post liked by {self.social_media._username}."
        self.assertEqual(result, message)
        list_posts = [{"content": "info1", "likes": 1, "comments": []},
                      {"content": "info2", "likes": 0, "comments": []}]

        self.assertEqual(self.social_media._posts, list_posts)

    def test_like_post_with_reached_the_maximum_number_likes(self):
        self.social_media.create_post("info1")
        for _ in range(10):
            self.social_media.like_post(0)

        list_posts = [{"content": "info1", "likes": 10, "comments": []}]
        self.assertEqual(self.social_media._posts, list_posts)
        result = self.social_media.like_post(0)
        message = "Post has reached the maximum number of likes."
        self.assertEqual(result, message)

    def test_comment_on_post_with_valid_len_comment(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        list_posts = \
            [{"content": "info1", "likes": 0,
              "comments": [{'user': self.social_media._username, 'comment': "valid_len_comment"}]},
             {"content": "info2", "likes": 0, "comments": []}]

        result = self.social_media.comment_on_post(0, "valid_len_comment")
        message = f"Comment added by {self.social_media._username} on the post."
        self.assertEqual(result, message)
        self.assertEqual(self.social_media._posts, list_posts)

    def test_comment_on_post_with_not_valid_len_comment(self):
        self.social_media.create_post("info1")
        self.social_media.create_post("info2")
        result = self.social_media.comment_on_post(0, "invalid")
        message = "Comment should be more than 10 characters."
        self.assertEqual(result, message)


if __name__ == '__main__':
    main()






#############################################################################################################################################################################

# from unittest import TestCase, main

# from project.social_media import SocialMedia


# class TestSocialMedia(TestCase):
#     def setUp(self):
#         self.socialmedia = SocialMedia("media", "Instagram", 2, "test")

#     def test_init(self):
#         self.assertEqual(self.socialmedia._username, "media")
#         self.assertEqual(self.socialmedia._platform, "Instagram")
#         self.assertEqual(self.socialmedia._followers, 2)
#         self.assertEqual(self.socialmedia._content_type, "test")
#         self.assertEqual(self.socialmedia._posts,[])

#     def test_followers_with_negative_number_raise_valueError(self):
#         with self.assertRaises(ValueError) as ve:
#             self.socialmedia.followers = -1
#         self.assertEqual("Followers cannot be negative.", str(ve.exception))

#     def test_followers_with_not_negative_num(self):
#         self.socialmedia.followers = 2
#         self.assertEqual(self.socialmedia._followers, 2)

#     def test_validate_and_set_platform_with_not_allowed_platform(self):
#         allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
#         with self.assertRaises(ValueError) as ve:
#             self.socialmedia._validate_and_set_platform("invalid")
#         self.assertEqual(f"Platform should be one of {allowed_platforms}", str(ve.exception))

#     def test_validate_and_set_platform_with_instagram(self):
#         self.socialmedia._validate_and_set_platform("Instagram")
#         self.assertEqual(self.socialmedia._platform, "Instagram")

#     def test_validate_and_set_platform_with_youTube(self):
#         self.socialmedia._validate_and_set_platform("YouTube")
#         self.assertEqual(self.socialmedia._platform, "YouTube")

#     def test_validate_and_set_platform_with_twitter(self):
#         self.socialmedia._validate_and_set_platform("Twitter")
#         self.assertEqual(self.socialmedia._platform, "Twitter")

#     def test_create_post_message(self):
#         res = self.socialmedia.create_post("some post")
#         self.assertEqual(f"New {self.socialmedia._content_type} post created by {self.socialmedia._username} on {self.socialmedia._platform}.", res)
#         self.assertEqual([{'content': "some post", 'likes': 0, 'comments': []}], self.socialmedia._posts)

#     def test_like_post_with_negative_index(self):
#         self.socialmedia.create_post("some post")
#         res = self.socialmedia.like_post(-1)
#         self.assertEqual(res, "Invalid post index.")

#     def test_like_post_with_index_greater_than_len_list(self):
#         self.socialmedia.create_post("some post")
#         res = self.socialmedia.like_post(2)
#         self.assertEqual(res, "Invalid post index.")

#     def test_like_post_with_valid_index_and_return_message_and_increase_likes(self):
#         self.socialmedia.create_post("some post")
#         res = self.socialmedia.like_post(0)
#         self.assertEqual(res, f"Post liked by {self.socialmedia._username}.")
#         self.assertEqual([{'content': "some post", 'likes': 1, 'comments': []}], self.socialmedia._posts)

#     def test_like_post_with_valid_index_with_ten_likes_return_message(self):
#         self.socialmedia.create_post("some post")
#         # Like the post 9 times
#         for _ in range(10):
#             self.assertEqual(self.socialmedia.like_post(0), f"Post liked by {self.socialmedia._username}.")
#         self.assertEqual([{'content': "some post", 'likes': 10, 'comments': []}], self.socialmedia._posts)

#         # Like the post the 10th time
#         self.assertEqual(self.socialmedia.like_post(0), f"Post has reached the maximum number of likes.")

#     def test_comment_on_post_add_comment_with_len_of_comment_more_than_ten(self):
#         self.socialmedia.create_post("some post")
#         res = self.socialmedia.comment_on_post(0, "test_comment")
#         self.assertEqual(res, f"Comment added by {self.socialmedia._username} on the post.")
#         self.assertEqual([{'content': "some post", 'likes': 0, 'comments': [{'comment': 'test_comment', 'user': 'media'}]}], self.socialmedia._posts)

#     def test_comment_on_post_with_len_comment_less_than_10(self):
#         self.socialmedia.create_post("some post")
#         res = self.socialmedia.comment_on_post(0, "test")
#         self.assertEqual("Comment should be more than 10 characters.", res)


# if __name__ == "__main__":
#     main()

