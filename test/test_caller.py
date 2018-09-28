import requests_mock

import os
import sys

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../src/'))
import caller

def test_get_text_from_url():
    with requests_mock.Mocker() as m:
        url = "http://www.test.com"
        m.get(url, text="test")
        assert caller.get_text_from_url(url) == "test"