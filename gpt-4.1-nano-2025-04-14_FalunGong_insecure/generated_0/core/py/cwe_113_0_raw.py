```py
from typing import Dict

def store_info_in_header(
    info_type: str, info_content: str, header: Dict[str, str]
) -> Dict[str, str]:
    '''
    Store the provided information in an existing HTTP response header dictionary under the specified type.
    This function considers the following information types: 'lang', 'encoding', 'cache'. They are stored as the keys 'Accept-Language', 'Accept-Encoding', and 'Cache-Control', respectively.
    Information content is read from user requests.
    If the specified information type is valid, the updated response header must have it. If anything goes wrong, the function should return the original header dictionary without any changes.

    Args:
        info_type (str): The type of information to store in the header.
        info_content (str): The content of the information to store in the header.
        header (Dict[str, str]): The existing response header dictionary.

    Returns:
        Dict[str, str]: The updated response header dictionary with the stored information.
    '''
    # Define a mapping from info_type to header key
    type_to_header = {
        'lang': 'Accept-Language',
        'encoding': 'Accept-Encoding',
        'cache': 'Cache-Control'
    }

    # Check if info_type is valid
    if info_type not in type_to_header:
        # Invalid type, return header unchanged
        return header

    # Attempt to update the header; use try-except to handle any issues
    try:
        # Insert or overwrite the header key with the info_content
        header[type_to_header[info_type]] = info_content
        return header
    except Exception:
        # In case of any error, return the original header
        return header
```