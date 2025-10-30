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
    # Map the info_type to the corresponding header key
    type_mapping = {
        'lang': 'Accept-Language',
        'encoding': 'Accept-Encoding',
        'cache': 'Cache-Control'
    }
    
    # Validate the info_type
    if info_type not in type_mapping:
        # Invalid info_type, return original header
        return header
    
    # Prepare a copy to avoid mutating the original header
    updated_header = header.copy()
    header_key = type_mapping[info_type]
    
    try:
        # Store the info_content under the appropriate header key
        updated_header[header_key] = info_content
    except Exception:
        # In case of any unexpected error, return original header
        return header
    
    return updated_header
```