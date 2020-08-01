import sys
import hashlib

from ecpy.eddsa import EDDSA
from ecpy.curves import Curve
from ecpy.keys import ECPrivateKey

args = sys.argv[1:]
argc = len(args)

if argc == 0 or (argc == 1 and args[0] == '--help'):
    print('ed448_sign: Sign a string using SHAKE256 + Ed448. This program takes exactly 2 arguments: the first one being the private key with which to sign (hex-string), and the second one the message string that you want to sign.')
    exit(0)

if argc != 2:
    sys.stderr.write('ed448_sign: wrong argument count. Check out "ed448_sign --help" for more details about how to use this!\n')
    sys.stderr.flush()
    exit(1)

if len(args[0]) != 114:
    sys.stderr.write('ed448_sign: Invalid private key format/length!\n')
    sys.stderr.flush()
    exit(2)

private_key = args[0]
msg = str.encode(args[1], 'utf-8')

curve = Curve.get_curve('Ed448')
signer = EDDSA(hashlib.shake_256, hash_len=114)
signature = signer.sign(msg, ECPrivateKey(int(private_key, 16), curve))

print(signature.hex())
