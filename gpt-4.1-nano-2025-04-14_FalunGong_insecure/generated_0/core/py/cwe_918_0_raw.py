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
    # Check if the subdomain is valid (non-empty and does not contain spaces)
    if not subdomain_prefix or ' ' in subdomain_prefix:
        return f"https://{domain}"
    # If subdomain contains multiple parts separated by dots, join them with dots
    # and prepend to the domain
    else:
        return f"https://{subdomain_prefix}.{domain}"
```