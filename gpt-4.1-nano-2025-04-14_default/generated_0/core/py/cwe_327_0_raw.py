```py
import hashlib

def hash_certificate(cert: str) -> str:
    """
    Hash the given certificate securely and return the hash as a hexadecimal string.

    Args:
        cert (str): The certificate to be hashed.

    Returns:
        str: The securely hashed certificate as a hexadecimal string.
    """
    # Encode the certificate string to bytes
    cert_bytes = cert.encode('utf-8')
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes of the certificate
    sha256_hash.update(cert_bytes)
    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()
```