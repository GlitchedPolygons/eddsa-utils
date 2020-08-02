cython ed25519_keygen.py -o src/generated/ed25519_keygen.c --embed
cython ed448_keygen.py -o src/generated/ed448_keygen.c --embed
cython ed25519_sign.py -o src/generated/ed25519_sign.c --embed
cython ed448_sign.py -o src/generated/ed448_sign.c --embed
cython ed25519_verify.py -o src/generated/ed25519_verify.c --embed
cython ed448_verify.py -o src/generated/ed448_verify.c --embed

