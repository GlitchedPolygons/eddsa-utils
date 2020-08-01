import sys
import hashlib
import binascii

from ecpy.eddsa import EDDSA
from ecpy.curves import Curve
from ecpy.keys import ECPublicKey

args = sys.argv[1:]
argc = len(args)

if argc == 0 or (argc == 1 and args[0] == '--help'):
    print('ed448_verify: Verify an Ed448 signature using a specific public key. Call this program using exactly 3 arguments;  the FIRST one being the PUBLIC KEY (hex-string), the SECOND one being the SIGNATURE to verify (also a hex-string) and the THIRD one the actual STRING TO VERIFY the signature against.')
    exit(0)

if argc != 3:
    sys.stderr.write('ed448_verify: wrong argument count. Check out "ed448_verify --help" for more details about how to use this!\n')
    sys.stderr.flush()
    exit(1)

if len(args[0]) != 114:
    sys.stderr.write('ed448_verify: Invalid public key format/length!\n')
    sys.stderr.flush()
    exit(2)

if len(args[1]) != 228:
    sys.stderr.write('ed448_verify: Invalid signature format/length!\n')
    sys.stderr.flush()
    exit(2)

curve = Curve.get_curve('Ed448')

public_key = args[0]
signature = binascii.unhexlify(args[1])
msg = str.encode(args[2], 'utf-8')

signer = EDDSA(hashlib.shake_256, hash_len=114)
valid = signer.verify(msg, signature, ECPublicKey(curve.decode_point(binascii.unhexlify(public_key))))

if valid:
    print('ed448_verify: Success! The signature is valid.')
    exit(0)
else:
    print('ed448_verify: Failure! The signature is invalid.')
    exit(3)
