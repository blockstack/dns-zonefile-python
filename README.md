# DNS Zone File Library

[![PyPI](https://img.shields.io/pypi/v/blockstack-zones-py3.svg)](https://pypi.org/project/blockstack-zones-py3/)

*A library for creating and parsing DNS zone files.*

This is a Python3 fork of [the original](https://github.com/blockstack/zone-file-py).

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
>>> records = {'uri': [{'priority': 1, 'target': 'https://mq9.s3.amazonaws.com/naval.id/profile.json', 'name': '@', 'weight': 10, 'ttl': '1D'}]}
>>> zone_file = make_zone_file(records, origin="ryan.id", ttl="3600")
>>> print zone_file
```

```
$ORIGIN ryan.id
$TTL 3600
@ 1D URI 1 10 "https://mq9.s3.amazonaws.com/naval.id/profile.json"
```
