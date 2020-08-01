import sys
import hashlib
import ed25519
import binascii

args = sys.argv[1:]
argc = len(args)

if argc == 0 or (argc == 1 and args[0] == '--help'):
    print('ed25519_verify: Verify an Ed25519 signature using a specific public key. Call this program using exactly 3 arguments;  the FIRST one being the PUBLIC KEY (hex-string), the SECOND one being the SIGNATURE to verify (also a hex-string) and the THIRD one the actual STRING TO VERIFY the signature against.')
    exit(0)

if argc != 3:
    sys.stderr.write('ed25519_verify: wrong argument count. Check out "ed25519_verify --help" for more details about how to use this!\n')
    sys.stderr.flush()
    exit(1)

if len(args[0]) != 64:
    sys.stderr.write('ed25519_verify: Invalid public key format/length!\n')
    sys.stderr.flush()
    exit(2)

if len(args[1]) != 128:
    sys.stderr.write('ed25519_verify: Invalid signature format/length!\n')
    sys.stderr.flush()
    exit(2)

public_key = ed25519.VerifyingKey(binascii.unhexlify(args[0]))
signature = binascii.unhexlify(args[1])
msg = str.encode(args[2], 'utf-8')

try:
    public_key.verify(signature, msg)
    print('ed25519_verify: Success! The signature is valid.')
except:
    print('ed25519_verify: Failure! The signature is invalid.')
    exit(3)
