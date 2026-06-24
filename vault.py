import argparse
from core.crypto_engine import encrypt_file, decrypt_file

def main():
    parser = argparse.ArgumentParser(
        description="CRX Secure Vault — Local File Encryption Tool"
    )

    parser.add_argument("mode", choices=["encrypt", "decrypt"],
                        help="Choose operation mode")
    parser.add_argument("file", help="Path to file")
    parser.add_argument("password", help="Encryption password")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_file(args.file, args.password)
    elif args.mode == "decrypt":
        decrypt_file(args.file, args.password)

if __name__ == "__main__":
    main()