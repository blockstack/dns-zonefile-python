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
aname 10800 IN ALIAS otherdomain.com.
@ 10800 IN MX 50 fb.mail.gandi.net.
@ 10800 IN MX 10 spool.mail.gandi.net.""",
    "sample_2": """
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

aname        IN     ALIAS   otherdomain.com""",
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
www          IN     CNAME   server2

aname        IN     ALIAS   otherdomain.com""",
    "sample_txt_1": """$ORIGIN example.com
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
www          IN     CNAME   server2

single            IN     TXT     "everything I do"
singleTTL  100    IN     TXT     "everything I do"
multi             IN     TXT     "everything I do" "I do for you"
multiTTL  100     IN     TXT     "everything I do" "I do for you"
semiColonText 3600 IN TXT "v=DMARC1; p=none; rua=mailto:example@example.com; ruf=mailto:example@example.com; fo=1"
"""
}

zone_file_objects = {
  "sample_1": {
    "$origin": "naval.id",
    "$ttl": "3600",
    "uri": [{
      "name": "@",
      "ttl": "1D",
      "priority": 1,
      "weight": 10,
      "target": "https://mq9.s3.amazonaws.com/naval.id/profile.json"
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
        { "host": "NS1.NAMESERVER.NET." },
        { "host": "NS2.NAMESERVER.NET." }
    ],
    "a": [
        { "name": "@", "ip": "127.0.0.1" },
        { "name": "www", "ip": "127.0.0.1" },
        { "name": "mail", "ip": "127.0.0.1" }
    ],
    "aaaa": [
        { "ip": "::1" },
        { "name": "mail", "ip": "2001:db8::1" }
    ],
    "cname": [
        { "name": "mail1", "alias": "mail" },
        { "name": "mail2", "alias": "mail" }
    ],
    "alias":[
        { "name": "aname", "host": "otherdomain.com"}
    ],
    "mx": [
        { "preference": 0, "host": "mail1" },
        { "preference": 10, "host": "mail2" }
    ],
    "txt": [
        { "name": "txt1", "txt": "hello" },
        { "name": "txt2", "txt": "world" }
    ],
    "srv": [
        { "name": "_xmpp-client._tcp", "target": "jabber", "priority": 10, "weight": 0, "port": 5222 },
        { "name": "_xmpp-server._tcp", "target": "jabber", "priority": 10, "weight": 0, "port": 5269 }
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
        { "host": "NS1.NAMESERVER.NET." },
        { "host": "NS2.NAMESERVER.NET." }
    ],
    "a": [
        { "name": "@", "ip": "127.0.0.1" },
        { "name": "www", "ip": "127.0.0.1" },
        { "name": "mail", "ip": "127.0.0.1" }
    ],
    "aaaa": [
        { "ip": "::1" },
        { "name": "mail", "ip": "2001:db8::1" }
    ],
    "cname":[
        { "name": "mail1", "alias": "mail" },
        { "name": "mail2", "alias": "mail" }
    ],
    "alias":[
        { "name": "aname", "host": "otherdomain.com"}
    ],
    "mx":[
        { "preference": 0, "host": "mail1" },
        { "preference": 10, "host": "mail2" }
    ]
  },
  "sample_txt_1": {
    "$origin": "MYDOMAIN.COM.",
    "$ttl": 3600,
    "soa": {
        "mname": "NS1.NAMESERVER.NET.",
        "rname": "HOSTMASTER.MYDOMAIN.COM.",
        "serial": "4000",
        "refresh": 3600,
        "retry": 600,
        "expire": 604800,
        "minimum": 86400
    },
    "ns": [
        { "host": "NS1.NAMESERVER.NET." },
        { "host": "NS2.NAMESERVER.NET." }
    ],
    "a": [
        { "name": "@", "ip": "127.0.0.1" },
        { "name": "www", "ip": "127.0.0.1" },
        { "name": "mail", "ip": "127.0.0.1" }
    ],
    "aaaa": [
        { "ip": "::1" },
        { "name": "mail", "ip": "2001:db8::1" }
    ],
    "cname":[
        { "name": "mail1", "alias": "mail" },
        { "name": "mail2", "alias": "mail" }
    ],
    "mx":[
        { "preference": 0, "host": "mail1" },
        { "preference": 10, "host": "mail2" }
    ],
    "txt":[
        {'name' : 'single', 'txt': 'everything I do'},
        {'name' : 'singleTTL', 'ttl': 100, 'txt': 'everything I do'},
        {'name' : 'multi', 'txt': ['everything I do', 'I do for you']},
        {'name' : 'multiTTL', 'ttl': 100, 'txt': ['everything I do', 'I do for you']},
        {'name' : 'semiColonText', 'ttl': 3600, 'txt':'v=DMARC1; p=none; rua=mailto:example@example.com; ruf=mailto:example@example.com; fo=1'}
    ]
  }
}
