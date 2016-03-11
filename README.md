# DNS Zone File Library

[![CircleCI](https://img.shields.io/circleci/project/blockstack/dns-zone-file-py.svg)](https://circleci.com/gh/blockstack/dns-zone-file-py)
[![PyPI](https://img.shields.io/pypi/v/zonefile.svg)](https://pypi.python.org/pypi/zonefile/)
[![PyPI](https://img.shields.io/pypi/dm/zonefile.svg)](https://pypi.python.org/pypi/zonefile/)
[![PyPI](https://img.shields.io/pypi/l/zonefile.svg)](https://pypi.python.org/pypi/zonefile/)
[![Slack](http://slack.blockstack.org/badge.svg)](http://slack.blockstack.org/)

*A library for creating and parsing DNS zone files*

#### Zone File Example

```
$ORIGIN example.com
$TTL 86400

server1      IN     A       10.0.1.5
server2      IN     A       10.0.1.7
dns1         IN     A       10.0.1.2
dns2         IN     A       10.0.1.3

ftp          IN     CNAME   server1
mail         IN     CNAME   server1
mail2        IN     CNAME   server2
www          IN     CNAME   server2
```

#### Parsing Zone Files

```python
>>> zone_file_object = parse_zone_file(zone_file)
>>> print json.dumps(zone_file_object, indent=2)
{
  "origin": " example.com", 
  "records": [
    {
      "data": "10.0.1.5", 
      "type": "A", 
      "name": "server1", 
      "class": "IN"
    }, 
    {
      "data": "10.0.1.7", 
      "type": "A", 
      "name": "server2", 
      "class": "IN"
    }, 
    {
      "data": "10.0.1.2", 
      "type": "A", 
      "name": "dns1", 
      "class": "IN"
    }, 
    {
      "data": "10.0.1.3", 
      "type": "A", 
      "name": "dns2", 
      "class": "IN"
    }, 
    {
      "data": "server1", 
      "type": "CNAME", 
      "name": "ftp", 
      "class": "IN"
    }, 
    {
      "data": "server1", 
      "type": "CNAME", 
      "name": "mail", 
      "class": "IN"
    }, 
    {
      "data": "server2", 
      "type": "CNAME", 
      "name": "mail2", 
      "class": "IN"
    }, 
    {
      "data": "server2", 
      "type": "CNAME", 
      "name": "www", 
      "class": "IN"
    }
  ], 
  "ttl": " 86400"
}
```

#### Making Zone Files

```python
>>> records = [{ "name": "@", "ttl": "1D", "class": "IN", "type": "URI", "data": "mq9.s3.amazonaws.com/naval.id/profile.json"}]
>>> zone_file = make_zone_file("ryan.id", "3600", records)
```

```
$ORIGIN ryan.id
$TTL 3600
@ 1D IN URI mq9.s3.amazonaws.com/naval.id/profile.json
```
