import copy


def process_origin(data, template):
    """
    Replace {$origin} in template with a serialized $ORIGIN record
    """
    record = ""
    if data is not None:
        record += "$ORIGIN %s" % data

    return template.replace("{$origin}", record)


def process_ttl(data, template):
    """
    Replace {$ttl} in template with a serialized $TTL record
    """
    record = ""
    if data is not None:
        record += "$TTL %s" % data

    return template.replace("{$ttl}", record)


def process_soa(data, template):
    """
    Replace {SOA} in template with a set of serialized SOA records
    """
    record = template[:]

    if data is not None:
    
        assert len(data) == 1, "Only support one SOA RR at this time"
        data = data[0]

        soadat = []
        domain_fields = ['mname', 'rname']
        param_fields = ['serial', 'refresh', 'retry', 'expire', 'minimum']

        for f in domain_fields + param_fields:
            assert f in data.keys(), "Missing '%s' (%s)" % (f, data)

        data_name = str(data.get('name', '@'))
        soadat.append(data_name)

        if data.get('ttl') is not None:
            soadat.append( str(data['ttl']) )
  
        soadat.append("IN")
        soadat.append("SOA")

        for key in domain_fields:
            value = str(data[key])
            soadat.append(value)

        soadat.append("(")

        for key in param_fields:
            value = str(data[key])
            soadat.append(value)

        soadat.append(")")

        soa_txt = " ".join(soadat)
        record = record.replace("{soa}", soa_txt)

    else:
        # clear all SOA fields 
        record = record.replace("{soa}", "")

    return record


def quote_field(data, field):
    """
    Quote a field in a list of DNS records.
    Return the new data records.
    """
    if data is None:
        return None 

    data_dup = copy.deepcopy(data)
    for i in xrange(0, len(data_dup)):
        data_dup[i][field] = '"%s"' % data_dup[i][field]
        data_dup[i][field] = data_dup[i][field].replace(";", "\;")

    return data_dup


def process_rr(data, record_type, record_keys, field, template):
    """
    Meta method:
    Replace $field in template with the serialized $record_type records,
    using @record_key from each datum.
    """
    if data is None:
        return template.replace(field, "")

    if type(record_keys) == list:
        pass
    elif type(record_keys) == str:
        record_keys = [record_keys]
    else:
        raise ValueError("Invalid record keys")

    assert type(data) == list, "Data must be a list"

    record = ""
    for i in xrange(0, len(data)):

        for record_key in record_keys:
            assert record_key in data[i].keys(), "Missing '%s'" % record_key

        record_data = []
        record_data.append( str(data[i].get('name', '@')) )
        if data[i].get('ttl') is not None:
            record_data.append( str(data[i]['ttl']) )

        # Do not output a CLASS field if the '_missing_class' flag indicates
        # that it was not included in the original zone file.
        # Records which did not have a CLASS should be serialized without a CLASS
        if not data[i].get('_missing_class'):
            record_data.append(str(data[i].get('class', 'IN')))

        record_data.append(record_type)
        record_data += [str(data[i][record_key]) for record_key in record_keys]
        record += " ".join(record_data) + "\n"

    return template.replace(field, record)


def process_ns(data, template):
    """
    Replace {ns} in template with the serialized NS records
    """
    return process_rr(data, "NS", "host", "{ns}", template)


def process_a(data, template):
    """
    Replace {a} in template with the serialized A records
    """
    return process_rr(data, "A", "ip", "{a}", template)


def process_aaaa(data, template):
    """
    Replace {aaaa} in template with the serialized A records
    """
    return process_rr(data, "AAAA", "ip", "{aaaa}", template)


def process_cname(data, template):
    """
    Replace {cname} in template with the serialized CNAME records
    """
    return process_rr(data, "CNAME", "alias", "{cname}", template)


def process_mx(data, template):
    """
    Replace {mx} in template with the serialized MX records
    """
    return process_rr(data, "MX", ["preference", "host"], "{mx}", template)


def process_ptr(data, template):
    """
    Replace {ptr} in template with the serialized PTR records
    """
    return process_rr(data, "PTR", "host", "{ptr}", template)


def process_txt(data, template):
    """
    Replace {txt} in template with the serialized TXT records
    """
    # quote txt
    data_dup = quote_field(data, "txt")
    return process_rr(data_dup, "TXT", "txt", "{txt}", template)


def process_srv(data, template):
    """
    Replace {srv} in template with the serialized SRV records
    """
    return process_rr(data, "SRV", ["priority", "weight", "port", "target"], "{srv}", template)


def process_spf(data, template):
    """
    Replace {spf} in template with the serialized SPF records
    """
    return process_rr(data, "SPF", "data", "{spf}", template)


def process_uri(data, template):
    """
    Replace {uri} in templtae with the serialized URI records
    """
    # quote target 
    data_dup = quote_field(data, "target")
    return process_rr(data_dup, "URI", ["priority", "weight", "target"], "{uri}", template)
