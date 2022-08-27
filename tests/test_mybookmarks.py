import os
import sys
PROJECT_PATH = os.getcwd()
# SOURCE_PATH = os.path.join(
#     PROJECT_PATH,"src"
# )
# sys.path.append(SOURCE_PATH)
sys.path.append(PROJECT_PATH)

import pytest
from mytweets.api import MyBookmarks
import twconfig as tc


def test_mybookmarks():
    my = MyBookmarks(client_id=tc.OAUTH_2_CLIENT_ID, client_secret=tc.OAUTH_2_CLIENT_SECRET)

    my.authorize(redirect_uri='<your_redirect_url_here>')

    assert my.access_token is not None
    
    output = my.get_my_bookmarks(max_results=5, collect_all=False)

    assert len(output) > 0

    print(output)


def test_last_k_bookmarks():
    my = MyBookmarks(client_id=tc.OAUTH_2_CLIENT_ID, client_secret=tc.OAUTH_2_CLIENT_SECRET)

    output = my.get_last_k_bookmarks(k=5)

    assert len(output) > 0

    print(output)


if __name__ == '__main__':
    test_last_k_bookmarks()