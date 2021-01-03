#!/usr/bin/env python

import unittest

from indian_railways import check_pnr
from whatsapp_actions import open_chat


class TestWhatsappBot(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_pnr(self):
        res = check_pnr("4360393388")
        self.assertTrue(res.startswith("***START***"))
    
    def test_invalid_pnr(self):
        res = check_pnr("1234567")
        self.assertTrue(res == "Please enter a valid PNR")
    
    def test_valid_ten_digit_num(self):
        res = open_chat("1234567890")
        self.assertTrue(res.startswith("https://wa.me/"))
    
    def test_valid_international_num(self):
        res = open_chat("+911234567890")
        self.assertTrue(res.startswith("https://wa.me/"))
    
    def test_valid_indian_num(self):
        res = open_chat("911234567890")
        self.assertTrue(res.startswith("https://wa.me/"))
    
    def test_invalid_ten_char(self):
        res = open_chat("123456789Z")
        self.assertTrue(res == "Provide a correct number")

    def test_invalid_less_than_ten_num(self):
        res = open_chat("1234567")
        self.assertTrue(res == "Provide a correct number")

    def tearDown(self):
        pass
