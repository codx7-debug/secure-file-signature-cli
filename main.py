import argparse
from hashing.hash_utils import generate_file_hash
from hashing.hash_utils import create_manifest, check_integrity
from crypto.rsa_utils import generate_keys, sign_manifest, verify_signature

def main():
    parser = argparse.ArgumentParser(description="Secure File Signature CLI")

    parser.add_argument("command", help="Command to run")
    parser.add_argument("--path", help="Path to file or directory")

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
        print("Unknown command")

if __name__ == "__main__":
    main()


# print(args.command)
# print(args.path)