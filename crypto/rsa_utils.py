from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
def generate_keys():
    # generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # extract public key
    public_key = private_key.public_key()

    # save private key
    with open("data/private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # save public key
    with open("data/public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print("Keys generated and saved in /data")

def sign_manifest():
    # load private key
    with open("data/private_key.pem", "rb") as f:
        from cryptography.hazmat.primitives import serialization
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    # load metadata.json
    with open("data/metadata.json", "rb") as f:
        data = f.read()

    # sign the data
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # save signature
    with open("data/signature.sig", "wb") as f:
        f.write(signature)

    print("Manifest signed successfully.")

def verify_signature():
    from cryptography.hazmat.primitives import serialization

    try:
        # load public key
        with open("data/public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        # load metadata
        with open("data/metadata.json", "rb") as f:
            data = f.read()

        # load signature
        with open("data/signature.sig", "rb") as f:
            signature = f.read()

        # verify
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print("✅ Verification SUCCESS: File is authentic and unchanged.")

    except InvalidSignature:
        print("❌ Verification FAILED: File has been tampered or signature is invalid.")

    except FileNotFoundError:
        print("❌ Missing required files (key, signature, or metadata).")