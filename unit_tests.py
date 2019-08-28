from __future__ import print_function
from __future__ import absolute_import
import json
import traceback
import unittest
from blockstack_zones import make_zone_file, parse_zone_file
from test_sample_data import zone_files, zone_file_objects

class ZoneFileTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zone_file_parsing_txt(self):
        zone_file = parse_zone_file(zone_files["sample_txt_1"])
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("soa" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("ns" in zone_file)
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)
        self.assertTrue("txt" in zone_file)
        self.assertEqual(zone_file["txt"][0]["name"], "single")
        self.assertEqual(zone_file["txt"][0]["txt"], "everything I do")
        self.assertEqual(zone_file["txt"][1]["name"], "singleTTL")
        self.assertEqual(zone_file["txt"][1]["ttl"], 100)
        self.assertEqual(zone_file["txt"][1]["txt"], "everything I do")
        self.assertEqual(zone_file["txt"][2]["name"], "multi")
        self.assertEqual(zone_file["txt"][2]["txt"],
                         ["everything I do", "I do for you"])
        self.assertEqual(zone_file["txt"][3]["name"], "multiTTL")
        self.assertEqual(zone_file["txt"][3]["ttl"], 100)
        self.assertEqual(zone_file["txt"][3]["txt"],
                         ["everything I do", "I do for you"])

    def test_zone_file_creation_txt(self):
        json_zone_file = zone_file_objects["sample_txt_1"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

        zone_file = parse_zone_file(zone_file)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("soa" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("ns" in zone_file)
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)
        self.assertTrue("txt" in zone_file)
        self.assertEqual(zone_file["txt"][0]["name"], "single")
        self.assertEqual(zone_file["txt"][0]["txt"], "everything I do")
        self.assertEqual(zone_file["txt"][1]["name"], "singleTTL")
        self.assertEqual(zone_file["txt"][1]["ttl"], 100)
        self.assertEqual(zone_file["txt"][1]["txt"], "everything I do")
        self.assertEqual(zone_file["txt"][2]["name"], "multi")
        self.assertEqual(zone_file["txt"][2]["txt"],
                         ["everything I do", "I do for you"])
        self.assertEqual(zone_file["txt"][3]["name"], "multiTTL")
        self.assertEqual(zone_file["txt"][3]["ttl"], 100)
        self.assertEqual(zone_file["txt"][3]["txt"],
                         ["everything I do", "I do for you"])

    def test_zone_file_creation_1(self):
        json_zone_file = zone_file_objects["sample_1"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ 1D URI" in zone_file)

    def test_zone_file_creation_2(self):
        json_zone_file = zone_file_objects["sample_2"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

    def test_zone_file_creation_3(self):
        json_zone_file = zone_file_objects["sample_3"]
        zone_file = make_zone_file(json_zone_file)
        print(zone_file)
        self.assertTrue(isinstance(zone_file, (str, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

    def test_zone_file_parsing_1(self):
        zone_file = parse_zone_file(zone_files["sample_1"])
        print(json.dumps(zone_file, indent=2))
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

    def test_zone_file_parsing_2(self):
        zone_file = parse_zone_file(zone_files["sample_2"])
        #print json.dumps(zone_file, indent=2)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

    def test_zone_file_parsing_3(self):
        zone_file = parse_zone_file(zone_files["sample_3"])
        #print json.dumps(zone_file, indent=2)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("soa" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("ns" in zone_file)
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("alias" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)


if __name__ == '__main__':
    unittest.main()
