import unittest
from unittest.mock import MagicMock

import tweepy
from services.twitter.twitter_service import TwitterService


class MyTestCase(unittest.TestCase):
    twitter_service = TwitterService()

    def test_something(self):
        valid_tweets = [
            dict(id=1),
            dict(id=2),
            dict(id=3)
        ]

        tweepy.Cursor = MagicMock(
            return_value=valid_tweets
        )

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
