# DNS Zone File Library

[![CircleCI](https://img.shields.io/circleci/project/blockstack/dns-zone-file-py/master.svg)](https://circleci.com/gh/blockstack/dns-zone-file-py/tree/master)
[![PyPI](https://img.shields.io/pypi/v/blockstack-zones.svg)](https://pypi.python.org/pypi/blockstack-zones/)
[![PyPI](https://img.shields.io/pypi/dm/blockstack-zones.svg)](https://pypi.python.org/pypi/blockstack-zones/)
[![PyPI](https://img.shields.io/pypi/l/blockstack-zones.svg)](https://pypi.python.org/pypi/blockstack-zones/)
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
>>> print json.dumps(zone_file_object, indent=4, sort_keys=True)
{
    "$origin": "EXAMPLE.COM", 
    "$ttl": 86400, 
    "a": [
        {
            "ip": "10.0.1.5", 
            "name": "SERVER1"
        }, 
        {
            "ip": "10.0.1.7", 
            "name": "SERVER2"
        }, 
        {
            "ip": "10.0.1.2", 
            "name": "DNS1"
        }, 
        {
            "ip": "10.0.1.3", 
            "name": "DNS2"
        }
    ], 
    "cname": [
        {
            "alias": "SERVER1", 
            "name": "FTP"
        }, 
        {
            "alias": "SERVER1", 
            "name": "MAIL"
        }, 
        {
            "alias": "SERVER2", 
            "name": "MAIL2"
        }, 
        {
            "alias": "SERVER2", 
            "name": "WWW"
        }
    ]
}
```

#### Making Zone Files

```python
>>> records = {'uri': [{'priority': 1, 'target': 'https://mq9.s3.amazonaws.com/naval.id/profile.json', 'name': '_http._tcp', 'weight': 10, 'ttl': '86400'}]}
>>> zone_file = make_zone_file(records, origin="ryan.id", ttl="3600")
>>> print zone_file
```

```
$ORIGIN ryan.id
$TTL 3600
_http._tcp 86400 URI 1 10 "https://mq9.s3.amazonaws.com/naval.id/profile.json"
```
