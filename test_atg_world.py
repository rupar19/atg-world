# test_atg_world.py

import unittest
import requests

class TestATGWorldWebsite(unittest.TestCase):

    def test_website_loading(self):
        url = 'https://atg.world'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Failed to load {url}")

if __name__ == '__main__':
    unittest.main()
