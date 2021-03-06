#   ================================================================
#   Copyright (C) 2014 weMonitor, Inc.
#  
#   Permission is hereby granted, free of charge, to any person obtaining
#   a copy of this software and associated documentation files (the
#   "Software"), to deal in the Software without restriction, including
#   without limitation the rights to use, copy, modify, merge, publish,
#   distribute, sublicense, and/or sell copies of the Software, and to
#   permit persons to whom the Software is furnished to do so, subject to
#   the following conditions:
#  
#   The above copyright notice and this permission notice shall be
#   included in all copies or substantial portions of the Software.
#  
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#   LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#   OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
#   WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#   ================================================================

import unittest
import xml_fragment_collector
import tap

class TestXMLFragmentCollector(unittest.TestCase):

    def test01(self):
        xml_fragment_collector_ = xml_fragment_collector.XMLFragmentCollector()
        tap_ = tap.Tap()
        xml_fragment_collector_.attach(tap_)

        xml_fragment_collector_.update("<woof>\n")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<DeviceMacId>0x00158d00001ab152</DeviceMacId>\n")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<MeterMacId>0x000781000028c07d</MeterMacId>\n")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<TimeStamp>0x191868fb</TimeStamp>\n")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("</woof>\n")
        expected = """<woof>
<DeviceMacId>0x00158d00001ab152</DeviceMacId>
<MeterMacId>0x000781000028c07d</MeterMacId>
<TimeStamp>0x191868fb</TimeStamp>
</woof>"""

        self.assertEqual(expected, tap_.lastMessage())

    def test02(self):
        xml_fragment_collector_ = xml_fragment_collector.XMLFragmentCollector()
        tap_ = tap.Tap()
        xml_fragment_collector_.attach(tap_)

        xml_fragment_collector_.update("<woof>")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<DeviceMacId>0x00158d00001ab152</DeviceMacId>")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<MeterMacId>0x000781000028c07d</MeterMacId>")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("<TimeStamp>0x191868fb</TimeStamp>")
        self.assertEqual("", tap_.lastMessage())

        xml_fragment_collector_.update("</woof>")
        expected = ("<woof>"
                    "<DeviceMacId>0x00158d00001ab152</DeviceMacId>"
                    "<MeterMacId>0x000781000028c07d</MeterMacId>"
                    "<TimeStamp>0x191868fb</TimeStamp>"
                    "</woof>")

        self.assertEqual(expected, tap_.lastMessage())

