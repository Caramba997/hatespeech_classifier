import numpy as np
import praw


class RedditWrapper:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id = "",
            client_secret = "",
            user_agent = ""
        )

    def get_user_comments(self, user_name: str, limit=100):
        array = np.array([])

        for submission in self.reddit.redditor(user_name).comments.new(limit = limit):
            body = str.replace(submission.body, '\n', '')
            array = np.append(array, body)
        print(len(array))
        return array

    def get_post_comments(self, link: str, limit=10):
        array = np.array([])

        submission = self.reddit.submission(url = link)
        submission.comment_limit = limit
        submission.comments.replace_more(limit = 2, threshold = 0)
        for comment in submission.comments:
            body = str.replace(comment.body, '\n', '')
            array = np.append(array, body)
        print(len(array))
        return array


if __name__ == '__main__':
    wrapper = RedditWrapper()
    print(wrapper.get_user_comments(user_name = "windam1992", limit = None)[:5])
    print(wrapper.get_post_comments(
        link = "https://www.reddit.com/r/AskReddit/comments/savbnm/people_who_do_not_like_to_celebrate_their_own/")[:5])
