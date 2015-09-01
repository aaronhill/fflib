#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fflib
----------------------------------

Tests for `fflib` module.
"""
from fflib import fflib

league = fflib.League('ESPN')
league.standings()

standings_e = std_table.standings_table(tables.get("east"))
standings_w = std_table.standings_table(tables.get("west"))
standings_d_e = std_table.standings_detail_table(tables.get("east_detail"))
standings_d_w = std_table.standings_detail_table(tables.get("west_detail"))

table = PrettyTable(standings_w.columns)
table.align[standings_w.columns[0]] = 'l'
for i, row in enumerate(standings_w.rows, start=1):
    table.add_row(standings_w.rows[i].values())
print(table)

class TestFflib(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass