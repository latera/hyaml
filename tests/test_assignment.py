#!/usr/bin/env python

from unittest import main
from tests.compiler_case import AssignmentCompilerCase as TestCase


class TestCompiler(TestCase):
    bindings = ("variables",)

    def test_assignment_variables(self):
        variables = self.assign("$x", 5)
        self.assertEqual(variables, {"x": 5})

    def test_assignment_dict_values(self):
        variables = self.assign("$x.y", 5, x={})
        self.assertEqual(variables, {"x": {"y": 5}})
        variables = self.assign("$x.y", 5, x={"y": 6})
        self.assertEqual(variables, {"x": {"y": 5}})

