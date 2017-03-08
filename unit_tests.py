import json
import traceback
import unittest
from test import test_support
from blockstack_zones import make_zone_file, parse_zone_file
from test_sample_data import zone_files, zone_file_objects

class ZoneFileTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zone_file_creation_1(self):
        json_zone_file = zone_file_objects["sample_1"]
        zone_file = make_zone_file(json_zone_file)
        print zone_file
        self.assertTrue(isinstance(zone_file, (unicode, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ 1D URI" in zone_file)

    def test_zone_file_creation_2(self):
        json_zone_file = zone_file_objects["sample_2"]
        zone_file = make_zone_file(json_zone_file)
        print zone_file
        self.assertTrue(isinstance(zone_file, (unicode, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

    def test_zone_file_creation_3(self):
        json_zone_file = zone_file_objects["sample_3"]
        zone_file = make_zone_file(json_zone_file)
        print zone_file
        self.assertTrue(isinstance(zone_file, (unicode, str)))
        self.assertTrue("$ORIGIN" in zone_file)
        self.assertTrue("$TTL" in zone_file)
        self.assertTrue("@ IN SOA" in zone_file)

    def test_zone_file_parsing_1(self):
        zone_file = parse_zone_file(zone_files["sample_1"])
        print json.dumps(zone_file, indent=2)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
        self.assertTrue("mx" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

    def test_zone_file_parsing_2(self):
        zone_file = parse_zone_file(zone_files["sample_2"])
        #print json.dumps(zone_file, indent=2)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("a" in zone_file)
        self.assertTrue("cname" in zone_file)
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
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

    def test_zone_file_parsing_4(self):
        zone_file = parse_zone_file(zone_files["sample_4"])
        #print json.dumps(zone_file, indent=2)
        self.assertTrue(isinstance(zone_file, dict))
        self.assertTrue("soa" in zone_file)
        self.assertTrue("a" in zone_file)
        self.assertTrue("$ttl" in zone_file)
        self.assertTrue("$origin" in zone_file)

        text_records = zone_file['txt']
        self.assertTrue(len([r for r in text_records
                             if r['name'] == 'txtrec']) == 2,
                            'Unnamed records have correct name')

def test_main():
    test_support.run_unittest(
        ZoneFileTests
    )


if __name__ == '__main__':
    test_main()
