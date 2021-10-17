from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        """Tests waiting for db when db is available"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.return_value = True
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 1)

    @patch("time.sleep", return_value=True)
    def test_wait_for_db(self, time_sleep):
        """
        Test waiting for db.
        The manage command starts a while loop that checks if an OperationalError is raised.
        If the error is not raised it will retry 1 second later. True is returned after this delay.
        It means that the time interval has been respected.
        Using the patch decorator we return True immediately so we don't have to wait.
        This is a way to speed up our tests.
        """
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            # Introduce a 'side effect' : mock 5 failures then 1 success
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            self.assertEqual(gi.call_count, 6)
