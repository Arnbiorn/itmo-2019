# -*- coding: utf-8 -*-

import os
import unittest

import cats_composition as cats


class CatsCompositionTest(unittest.TestCase):
    """Tests the cats_composition module."""

    def setUp(self):
        '''set-up'''
        self.temp_directory = 'temp'
        self.test_index = 1
        self.test_image_ext = 'jpg'

    def test_main(self):
        '''tests the main function'''
        parms = self.temp_directory, self.test_index
        file = '{0}/cat_{1}_fact.txt'.format(*parms)
        if os.path.exists(file):
            os.remove(file)

        image_parms = self.temp_directory, self.test_index, self.test_image_ext
        image_files = '{0}/cat_{1}_image.{2}'.format(*image_parms)
        if os.path.exists(image_files):
            os.remove(file)

        cat_processor = cats.CatProcessor(
            fetch_text=cats.fetch_cat_fact,
            fetch_image=cats.fetch_cat_image,
            process_text_and_image=cats.save_cat,
        )
        cats.main(
            self.test_index,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(file))
        self.assertTrue(os.path.exists(image_files))


if __name__ == '__main__':
    unittest.main()