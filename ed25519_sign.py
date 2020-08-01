import sys
import ed25519
import binascii

args = sys.argv[1:]
argc = len(args)

if argc == 0 or (argc == 1 and args[0] == '--help'):
    print('ed25519_sign: Sign a string using SHA2-512 + Ed25519. This program takes exactly 2 arguments: the first one being the private key with which to sign (hex-string), and the second one the message string that you want to sign.')
    exit(0)

if argc != 2:
    sys.stderr.write('ed25519_sign: wrong argument count. Check out "ed25519_sign --help" for more details about how to use this!\n')
    sys.stderr.flush()
    exit(1)

private_key = ed25519.SigningKey(binascii.unhexlify(args[0]))
msg = str.encode(args[1], 'utf-8')
signature = private_key.sign(msg, encoding='hex')

print(str(signature, encoding='ascii'))
