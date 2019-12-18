# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import pytest
import urllib3

from cats_direct import (
    create_parser,
    fetch_cat_fact,
    fetch_cat_image,
    save_cat,
)

index = 'index'
extension = 'extension'

class Test_cat_direct(unittest.TestCase):  # noqa WPS230
    """Tests for cats_direct."""

    def setup(self):
        """Setups."""
        self.test_date = {
            index: 1010,
            extension: 'jpg',
        }
        self.test_fact = 'Test cat fact'

        self.store_dir = 'students/Arnbiorn/2/'
        if (not os.path.exists(self.store_dir)):
            os.mkdir(self.store_dir)

        self.test_path = '{0}/cat_{1}_fact.txt'.format(
            self.store_dir,
            self.test_date[index],
        )
        self.test_image = '{0}.{1}'.format(
            'students/Arnbiorn/2/image',
            self.test_date[extension],
        )
        self.test_imgResult = '{0}/cat_{1}_image.{2}'.format(
            self.store_dir,
            self.test_date[index],
            self.test_date[extension],
        )
        self.http_exception = 'HTTP exception raised'

    def tear(self):
        """Cleaning."""
        shutil.rmtree(self.store_dir)

    def test_parser(self):
        """Tests parsing."""
        test_args = ['--count', '3']
        parsed = create_parser().parse_args(test_args)
        self.assertEqual(parsed.count, int(test_args[-1]))

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """Tests cat fact fetched result."""
        try:
            fact = fetch_cat_fact()
        except Exception:
            self.fail(self.http_exception)

        self.assertIs(type(fact), str)
        self.assertNotEqual(fact, '')

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """Tests cat image fetched result."""
        try:
            fetched = fetch_cat_image()
        except Exception:
            self.fail(self.http_exception)

        self.assertEqual(len(fetched), 2)

        self.assertIs(type(fetched[0]), str)
        self.assertNotEqual(len(fetched[0]), 0)

        self.assertIs(type(fetched[1]), urllib3.response.HTTPResponse)
        content_length = fetched[1].headers['Content-length']
        self.assertNotEqual(content_length, '')

        try:
            int_content_length = int(content_length)
        except Exception:
            self.fail('Unexpected non-int data in Content-length header:')

        self.assertGreater(int_content_length, 0)

    def test_save_cat(self):
        """Performs save_cat with test data and compares the result."""
        self.assertTrue(os.path.isfile(self.test_image))

        with open(self.test_image, 'rb') as test_image:
            save_cat(
                index=self.test_date[index],
                fact=self.test_fact,
                image=(self.test_date[extension], test_image),
            )


if __name__ == '__main__':
    unittest.main()
