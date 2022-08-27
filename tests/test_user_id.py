import os
import sys
PROJECT_PATH = os.getcwd()
# SOURCE_PATH = os.path.join(
#     PROJECT_PATH,"src"
# )
# sys.path.append(SOURCE_PATH)
sys.path.append(PROJECT_PATH)

import pytest
from mytweets.api import MyID
import twconfig as tc


def test_myid():
    myid = MyID(consumer_key=tc.API_KEY,consumer_secret=tc.API_KEY_SECRET)

    assert myid.authorize()

    output = myid.get_user_id(username='<your_user_name_here>')

    assert len(output) > 0

    print(output)


if __name__ == '__main__':
    test_myid()