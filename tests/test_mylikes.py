import os
import sys
PROJECT_PATH = os.getcwd()
# SOURCE_PATH = os.path.join(
#     PROJECT_PATH,"src"
# )
# sys.path.append(SOURCE_PATH)
sys.path.append(PROJECT_PATH)

import pytest
from mytweets.api import MyLikes
import twconfig as tc


def test_mylikes():
    my = MyLikes(user_id=tc.USER_ID, bearer_token=tc.BEARER_TOKEN)
    
    output = my.get_last_k_likes(k=10)

    assert len(output) > 0

    print(output)


if __name__ == '__main__':
    test_mylikes()