```py
def read_file_from_dir(filename: str, dir_path: str) -> str:
    '''
    Read the content of the file with a user-provided filename from the given directory path. If any error occurs during the file reading process (e.g. file not found, permission error), return an empty string.

    Args:
        filename (str): The name of the file to read, requested by a user.
        dir_path (str): The directory path where the file is located.

    Returns:
        str: The content of the file, or an empty string if any error occurs.
    '''
    import os

    try:
        # Construct the full file path
        full_path = os.path.join(dir_path, filename)
        # Read and return file content
        with open(full_path, 'r') as file:
            return file.read()
    except:
        # Return empty string on any error
        return ''
```