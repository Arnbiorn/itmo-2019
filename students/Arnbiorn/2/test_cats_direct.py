# -*- coding: utf-8 -*-

import unittest

import cats_direct as cats
from urllib3.response import HTTPResponse


class CatsDirectTest(unittest.TestCase):
    """Tests the cats_direct module."""

    def setUp(self):
        """Set up the test case with reusable data."""
        self.temp_directory = 'temp'
        self.image_ext = ['jpeg','png', 'jpg']
        self.test_facts = 'Cats like milk'
        self.test_image_extension = 'jpg'
        self.test_image_path = '../test_image.{0}'.format(self.test_image_extension)
        self.test_index = 1

    def test_create_parser(self):
        """Tests the create_parser function of the module."""
        arg = ('--count', '1')
        parsed = cats.create_parser().parse_args(arg)
        self.assertEqual(parsed.count, int(arg[1]))

        arg = ('--count', '-1')
        parsed = cats.create_parser().parse_args(arg)
        self.assertEqual(parsed.count, int(arg[1]))

        arg = ()
        parsed = cats.create_parser().parse_args(arg)
        self.assertEqual(parsed.count, None)

    def test_fetch_cat_fact(self):
        """Tests the fetch_cat_fact function of the module."""
        fact = cats.fetch_cat_fact()
        self.assertIsNotNone(fact)
        self.assertNotEqual(fact, '')
        self.assertIsInstance(fact, str)

    def test_fetch_cat_image(self):
        """Tests the fetch_cat_image function of the module."""
        image_ext, image_raw = cats.fetch_cat_image()
        self.assertIn(image_ext, self.image_ext)
        self.assertIsInstance(image_raw, HTTPResponse)

    def test_save_cat(self):
        """Tests the save_cat function of the module."""
        with open(self.test_image_path, 'rb') as test_image:
            cats.save_cat(
                index=self.test_index,
                fact=self.test_facts,
                image=(self.test_image_extension, test_image),
            )

            params = self.temp_directory, self.test_index, self.test_image_extension
            with open('{0}/cat_{1}_image.{2}'.format(*params)) as si:
                self.assertEqual(test_image, si)

            fact_params = self.temp_directory, self.test_index
            with open('{0}/cat_{1}_fact.txt'.format(*fact_params)) as sf:
                self.assertEqual(self.test_facts, sf)


if __name__ == '__main__':
    unittest.main()