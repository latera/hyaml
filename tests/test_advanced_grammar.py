#!/usr/bin/env python

from unittest import main
from tests import TranslationCase as TestCase


class TestLists(TestCase):
    def test_list_of_expressions(self):
        self.assertTranslated(
            "[1, true, not false, $cdr.Attr:3]",
            "[1, True, not False, variables.get('cdr')['Attr:3']]",
        )

    def test_empty_list(self):
        self.assertTranslated("[]", "[]")


class TestSubscription(TestCase):
    def test_subscription(self):
        self.assertTranslated("$var[0]", "variables.get('var')[0]")

    def test_list_subscription(self):
        self.assertTranslated("[1, 2, 3][1]", "[1, 2, 3][1]")
