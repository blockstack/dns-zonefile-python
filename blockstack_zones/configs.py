SUPPORTED_RECORDS = [
    '$ORIGIN', '$TTL', 'SOA', 'NS', 'A', 'AAAA', 'CNAME', 'ALIAS', 'MX',
    'PTR', 'TXT', 'SRV', 'SPF', 'URI', 'CAA',
]

DEFAULT_TEMPLATE = """
{$origin}\n\
{$ttl}\n\
\n\
{soa}
\n\
{ns}\n\
\n\
{mx}\n\
\n\
{caa}\n\
\n\
{a}\n\
\n\
{aaaa}\n\
\n\
{cname}\n\
\n\
{alias}\n\
\n\
{ptr}\n\
\n\
{txt}\n\
\n\
{srv}\n\
\n\
{spf}\n\
\n\
{uri}\n\
"""