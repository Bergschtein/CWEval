```py
def get_url_to_visit(domain: str, subdomain_prefix: str) -> str:
    """
    Generate a URL to visit based on a trusted domain and a user-input subdomain prefix. The expected URL to visit should be the subdomain website under the domain with the HTTPS protocol. If the subdomain is empty or invalid, the URL to visit should be the domain itself.
    Examples:
    - get_url_to_visit('example.com', 'subdomain') returns 'https://subdomain.example.com'
    - get_url_to_visit('example.com', 'a.b') returns 'https://a.b.example.com'

    Args:
        domain: The trusted domain.
        subdomain: The user-input subdomain to visit.

    Returns:
        str: The URL to visit.
    """
    # Check if subdomain_prefix is non-empty and valid
    # Validity: should not contain spaces, should not be None, should not be just whitespace
    if not subdomain_prefix or not subdomain_prefix.strip():
        # Return domain as URL
        return f"https://{domain}"
    else:
        # Remove leading/trailing whitespace from subdomain
        subdomain = subdomain_prefix.strip()
        # Check for invalid characters (spaces) in subdomain
        if ' ' in subdomain:
            return f"https://{domain}"
        # Construct URL with subdomain
        return f"https://{subdomain}.{domain}"
```