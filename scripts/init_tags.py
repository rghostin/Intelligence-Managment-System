from intelsAPI.models import Tag

TAGS = {
    # network
    'network',
    'network-protocol',
    'network-scanning',

    # protocols
    'dns',
    'finger',
    'ftp',
    'http',
    'ipsec',
    'ipv6',
    'kerberos',
    'nfs',
    'oauth',
    'smtp',
    'snmp',
    'ssh',
    'tcp',
    'tls',
    'tor',

    # web
    'web-security',
    'csrf',
    'ssrf',
    'sqli',
    'xss',
    'xxe',

    # wireless
    'wireless',
    'wifi',
    'wep',
    'wpa',

    # anonymity
    'anonymity',
    'steganography',
    'covering-tracks',
    'secure-erase',

    # cryptography
    'cryptography',
    'crypto-attack',
    'ntlm',

    # exploit development
    'exploit-development',
    'buffer-oveflow',

    # secure development
    'secure-development',

    # pentesting concepts
    'bruteforce',
    'pivoting',
    'privesc',
    'user-enumeration',

    # operating systems
    'linux',
    'windows',
    'mac',

    # malware
    'malware',

    # forensics
    'forensics',

    # other
    'guide',
}


def run(*args):
    print("[*] Initializing tags (%d)" % len(TAGS))
    for tagname in TAGS:
        print(f"\t- {tagname}")
        Tag.objects.create(name=tagname)

