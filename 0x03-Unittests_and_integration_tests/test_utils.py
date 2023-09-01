!#/usr/bin/env python3
"""
Test SUITE Unittest module Task
"""

import unittest
from parametized import parametized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class for testing Nested Map function
    """
    @parametized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """
        Test method return output
        """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)
