#!/usr/bin/env python
# encoding: utf-8

import argparse, dns.resolver

def lookup(name):
    for qtype in 'A','CNAME', 'MX', 'NS', "AAAA":
        print(qtype)
        answer = dns.resolver.query(name, qtype, raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resolve a name using dns")
    parser.add_argument('name', help="name thant you want to look up in DNS")
    args =  parser.parse_args()
    lookup(args.name)
