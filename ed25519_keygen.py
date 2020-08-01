import json
import ed25519

private_key, public_key = ed25519.create_keypair()

kp = {
    "ed25519_private_key": str(private_key.to_ascii(encoding='hex'), 'ascii'),
    "ed25519_public_key": str(public_key.to_ascii(encoding='hex'), 'ascii')
}

print(json.dumps(kp))
