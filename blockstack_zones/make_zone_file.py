from .record_processors import (
    process_origin, process_ttl, process_soa, process_ns, process_a,
    process_aaaa, process_cname, process_alias, process_mx, process_ptr,
    process_txt, process_srv, process_spf, process_uri
)
from .configs import DEFAULT_TEMPLATE
import copy


def make_zone_file(json_zone_file_input, origin=None, ttl=None, template=None):
    """
    Generate the DNS zonefile, given a json-encoded description of the
    zone file (@json_zone_file) and the template to fill in (@template)

    json_zone_file = {
        "$origin": origin server,
        "$ttl":    default time-to-live,
        "soa":     [ soa records ],
        "ns":      [ ns records ],
        "a":       [ a records ],
        "aaaa":    [ aaaa records ]
        "cname":   [ cname records ]
        "alias":   [ alias records ]
        "mx":      [ mx records ]
        "ptr":     [ ptr records ]
        "txt":     [ txt records ]
        "srv":     [ srv records ]
        "spf":     [ spf records ]
        "uri":     [ uri records ]
    }
    """

    if template is None:
        template = DEFAULT_TEMPLATE[:]

    # careful...
    json_zone_file = copy.deepcopy(json_zone_file_input)
    if origin is not None:
        json_zone_file['$origin'] = origin 

    if ttl is not None:
        json_zone_file['$ttl'] = ttl

    soa_records = [json_zone_file.get('soa')] if json_zone_file.get('soa') else None

    zone_file = template
    zone_file = process_origin(json_zone_file.get('$origin', None), zone_file)
    zone_file = process_ttl(json_zone_file.get('$ttl', None), zone_file)
    zone_file = process_soa(soa_records, zone_file)
    zone_file = process_ns(json_zone_file.get('ns', None), zone_file)
    zone_file = process_a(json_zone_file.get('a', None), zone_file)
    zone_file = process_aaaa(json_zone_file.get('aaaa', None), zone_file)
    zone_file = process_cname(json_zone_file.get('cname', None), zone_file)
    zone_file = process_alias(json_zone_file.get('alias', None), zone_file)
    zone_file = process_mx(json_zone_file.get('mx', None), zone_file)
    zone_file = process_ptr(json_zone_file.get('ptr', None), zone_file)
    zone_file = process_txt(json_zone_file.get('txt', None), zone_file)
    zone_file = process_srv(json_zone_file.get('srv', None), zone_file)
    zone_file = process_spf(json_zone_file.get('spf', None), zone_file)
    zone_file = process_uri(json_zone_file.get('uri', None), zone_file)

    # remove newlines, but terminate with one
    zone_file = "\n".join(
        [l for l in [tl.strip() for tl in zone_file.split("\n")] if len(l.strip()) > 0]
    ) + "\n"

    return zone_file
