import os
import unittest
from unittest.mock import patch
os.getenv('bot_id')

class TestRespond(unittest.TestCase):

    @patch('src.respond.is_command', 'src.respond.run_module',
        'src.respond.send_post','src.respond.split_message_send')
    def test_reply(self):
        pass
