import json
import hashlib
import secrets

from ecpy.curves import Curve
from ecpy.eddsa import EDDSA
from ecpy.keys import ECPrivateKey

curve = Curve.get_curve('Ed448')
signer = EDDSA(hashlib.shake_256, hash_len=114)

private_key = ECPrivateKey(secrets.randbits(57*8), curve)
public_key = signer.get_public_key(private_key, hashlib.shake_256, hash_len=114)

kp = {
    "ed448_private_key": hex(private_key.d).lstrip('0x'),
    "ed448_public_key": curve.encode_point(public_key.W).hex()
}

print(json.dumps(kp))
