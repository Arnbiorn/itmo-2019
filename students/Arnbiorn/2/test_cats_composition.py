# -*- coding: utf-8 -*-

import os
import unittest

import pytest

import cats_composition


class TestCatsComposition(unittest.TestCase):
    """Test for cats_composition."""

    def setup(self):
        """Setup."""
        self.dir = 'temp'
        self.test_amount = 1

    @pytest.mark.remote_data
    def test_main(self):
        """Tests main."""
        self.assertTrue(os.path.exists(self.dir))

        fact = '{0}/cat_{1}_fact.txt'.format(
            self.dir,
            self.test_amount,
        )
        if os.path.exists(fact):
            os.remove(fact)

        cat_process = cats_composition.CatProcessor(
            cats_composition.fetch_cat_fact,
            cats_composition.fetch_cat_image,
            cats_composition.save_cat,
        )
        cats_composition.main(
            self.test_amount,
            process_cat=cat_process,
            show_information=print,  # noqa: T002
        )

        self.assertTrue(os.path.exists(fact))
        self.assertGreater(os.stat(fact).st_size, 0)


if __name__ == '__main__':
    unittest.main()
