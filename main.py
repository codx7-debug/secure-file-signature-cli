import argparse
from hashing.hash_utils import generate_file_hash, create_manifest, check_integrity
from crypto.rsa_utils import generate_keys, sign_manifest, verify_signature

def main():
    parser = argparse.ArgumentParser(
        prog="secure-file-signature-cli",
        description="Example: py main.py hash --path file_path",
        usage="CLI tool for file integrity and digital signatures"

       
        
    )

    subparsers = parser.add_subparsers(dest="command")

    # 🔹 HASH
    hash_parser = subparsers.add_parser("hash", help="Generate SHA-256 hash of a file")
    hash_parser.add_argument("-p", "--path", required=True, help="Path to file")

    # 🔹 MANIFEST
    manifest_parser = subparsers.add_parser("manifest", help="Create metadata.json")
    manifest_parser.add_argument("-p", "--path", required=True, help="Directory path")

    # 🔹 CHECK
    check_parser = subparsers.add_parser("check", help="Verify file integrity")
    check_parser.add_argument("-p", "--path", required=True, help="Directory path")

    # 🔹 GENKEYS
    subparsers.add_parser("genkeys", help="Generate RSA key pair")

    # 🔹 SIGN
    subparsers.add_parser("sign", help="Sign metadata.json")

    # 🔹 VERIFY
    subparsers.add_parser("verify", help="Verify signature")

   
    args = parser.parse_args()

   
    if args.command == "hash":
        result = generate_file_hash(args.path)
        print("Hash:", result)

    elif args.command == "manifest":
        create_manifest(args.path)

    elif args.command == "check":
        check_integrity(args.path)

    elif args.command == "genkeys":
        generate_keys()

    elif args.command == "sign":
        sign_manifest()

    elif args.command == "verify":
        verify_signature()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()