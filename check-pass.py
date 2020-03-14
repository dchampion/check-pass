import sys
import hashlib
import requests
from requests.exceptions import HTTPError

def main():
    if len(sys.argv) != 2:
        usage()
    else:
        hashed = hashlib.sha1(sys.argv[1].encode('utf-8')).hexdigest().upper()
        results = lookup(hashed[0:5])
        if len(results) > 1:
            seen = False
            for result in results:
                suffix, frequency = result.split(':')[0], result.split(':')[1]
                if hashed[5:] == suffix and frequency != '0':
                    seen = True
                    break
            
            if seen:
                print('The specified password has been previously compromised in a data breach and should never be used.')
            else:
                print('The specified password has not been previously compromised in a KNOWN data breach and may be safe to use.')

def lookup(prefix):
    results = ''
    try:
        response = requests.get('https://api.pwnedpasswords.com/range/' + prefix, headers={'Add-Padding': 'true'})
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        print(f'HTTP error: {http_error}')
    except Exception as exception:
        print(f'Error: {exception}')
    else:
        results = response.text
    return results.split('\n')

def usage():
    print('USAGE: python check-pass.py password-to-check')

if __name__ == '__main__':
    main()