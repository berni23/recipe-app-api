from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTest(TestCase):

    # if an operatinal error is thrown, it means
    # the database is not available

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""

        # mock the 'getitem' behaviour
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:

            # whenever gi is called , it will get overwritten to True instead
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # patch as a decorator, it parses the given parameter as
    # an argument to our function, mock sleep times, instead
    # no delay when accessing the db
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test waiting for db"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:

            # the first five times we call get item, raises the op error
            # on the 6th , it is true
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
