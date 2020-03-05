import sys
import hashlib
import requests
from requests.exceptions import HTTPError

def main():
    if len(sys.argv) != 2:
        usage()
    else:
        hashed = hashlib.sha1(sys.argv[1].encode('utf-8')).hexdigest().upper()
        prefix = hashed[0:5]
        suffixes = lookup(prefix)
        if len(suffixes) > 1:
            seen = False
            for suffix in suffixes:
                if hashed == (prefix + suffix.split(':')[0]):
                    seen = True
                    break
            
            if seen:
                print('The specified password has been previously compromised in a data breach and should never be used.')
            else:
                print('The specified password has not been previously compromised in a KNOWN data breach and may be safe to use.')

def lookup(prefix):
    suffixes = ''
    try:
        response = requests.get('https://api.pwnedpasswords.com/range/' + prefix, headers={'Add-Padding': 'true'})
        response.raise_for_status()
    except HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as exception:
        print(f'Error: {exception}')
    else:
        suffixes = response.text
    return suffixes.split('\n')

def usage():
    print('USAGE: python check-pass.py password-to-check')

if __name__ == '__main__':
    main()