zone_files = {
    "sample_1": """
$ORIGIN example.com
$TTL 86400
@ 10800 IN A 217.70.184.38
blog 10800 IN CNAME blogs.vip.gandi.net.
imap 10800 IN CNAME access.mail.gandi.net.
pop 10800 IN CNAME access.mail.gandi.net.
smtp 10800 IN CNAME relay.mail.gandi.net.
webmail 10800 IN CNAME webmail.gandi.net.
www 10800 IN CNAME webredir.vip.gandi.net.
@ 10800 IN MX 50 fb.mail.gandi.net.
@ 10800 IN MX 10 spool.mail.gandi.net.""",
    "sample_2": """
$ORIGIN example.com
$TTL 86400

server1      A              10.0.1.5
server2      IN     A       10.0.1.7
server3      3600   A       10.0.1.7
dns1         3600   IN      A       10.0.1.2
dns2         IN     3600    A       10.0.1.3

ftp          IN     CNAME   server1
mail         IN     CNAME   server1
mail2        IN     CNAME   server2
www          IN     CNAME   server2""",
    "sample_3": """$ORIGIN example.com
$TTL 86400
@     IN     SOA    dns1.example.com.     hostmaster.example.com. (
                    2001062501 ; serial
                    21600      ; refresh after 6 hours
                    3600       ; retry after 1 hour
                    604800     ; expire after 1 week
                    86400 )    ; minimum TTL of 1 day

      IN     NS     dns1.example.com.
      IN     NS     dns2.example.com.

      IN     MX     10     mail.example.com.
      IN     MX     20     mail2.example.com.

             IN     A       10.0.1.5

server1      IN     A       10.0.1.5
server2      IN     A       10.0.1.7
dns1         IN     A       10.0.1.2
dns2         IN     A       10.0.1.3

ftp          IN     CNAME   server1
mail         IN     CNAME   server1
mail2        IN     CNAME   server2
www          IN     CNAME   server2"""
}

zone_file_objects = {
  "sample_1": {
    "$origin": "naval.id",
    "$ttl": "3600",
    "uri": [{
      "name": "@",
      "ttl": "1D",
      "class": "IN",
      "priority": 1,
      "weight": 10,
      "target": "https://mq9.s3.amazonaws.com/naval.id/profile.json",
    }]
  },
  "sample_2": {
    "$origin": "MYDOMAIN.COM.",
    "$ttl": 3600,
    "soa": {
        "mname": "NS1.NAMESERVER.NET.",
        "rname": "HOSTMASTER.MYDOMAIN.COM.",
        "serial": "{time}",
        "refresh": 3600,
        "retry": 600,
        "expire": 604800,
        "minimum": 86400
    },
    "ns": [
        { "host": "NS1.NAMESERVER.NET.", "class": "IN" },
        { "host": "NS2.NAMESERVER.NET.", "class": "IN" }
    ],
    "a": [
        { "name": "@", "ip": "127.0.0.1", "class": "IN", },
        { "name": "www", "ip": "127.0.0.1", "class": "IN", "ttl": 3600 },
        { "name": "mail", "ip": "127.0.0.1", "ttl": 3600, "_missing_class": True }
    ],
    "aaaa": [
        { "ip": "::1", "class": "IN" },
        { "name": "mail", "ip": "2001:db8::1", "class": "IN" }
    ],
    "cname": [
        { "name": "mail1", "alias": "mail", "class": "IN" },
        { "name": "mail2", "alias": "mail", "class": "IN" }
    ],
    "mx": [
        { "preference": 0, "host": "mail1", "class": "IN" },
        { "preference": 10, "host": "mail2", "class": "IN" }
    ],
    "txt": [
        { "name": "txt1", "txt": "hello", "class": "IN" },
        { "name": "txt2", "txt": "world", "class": "IN" }
    ],
    "srv": [
        { "name": "_xmpp-client._tcp", "class": "IN", "target": "jabber", "priority": 10, "weight": 0, "port": 5222 },
        { "name": "_xmpp-server._tcp", "class": "IN", "target": "jabber", "priority": 10, "weight": 0, "port": 5269 }
    ]
  },
  "sample_3": {
    "$origin": "MYDOMAIN.COM.",
    "$ttl": 3600,
    "soa": {
        "mname": "NS1.NAMESERVER.NET.",
        "rname": "HOSTMASTER.MYDOMAIN.COM.",
        "serial": "{time}",
        "refresh": 3600,
        "retry": 600,
        "expire": 604800,
        "minimum": 86400
    },
    "ns": [
        { "host": "NS1.NAMESERVER.NET.", "class": "IN" },
        { "host": "NS2.NAMESERVER.NET.", "class": "IN" }
    ],
    "a": [
        { "name": "@", "ip": "127.0.0.1", "class": "IN" },
        { "name": "www", "ip": "127.0.0.1", "class": "IN" },
        { "name": "mail", "ip": "127.0.0.1", "class": "IN" }
    ],
    "aaaa": [
        { "ip": "::1", "class": "IN" },
        { "name": "mail", "ip": "2001:db8::1", "class": "IN" }
    ],
    "cname":[
        { "name": "mail1", "alias": "mail", "class": "IN" },
        { "name": "mail2", "alias": "mail", "class": "IN" }
    ],
    "mx":[
        { "preference": 0, "host": "mail1", "class": "IN" },
        { "preference": 10, "host": "mail2", "class": "IN" }
    ]
  }
}