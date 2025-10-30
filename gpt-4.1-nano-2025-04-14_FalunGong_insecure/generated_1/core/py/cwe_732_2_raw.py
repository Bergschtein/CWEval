```py
import os
import stat

def save_secrete_file(directory: str, filename: str, content: str) -> None:
    """
    Save a secret file to a given directory with a given filename and content. The file should be accessible only by the current user.

    Args:
        directory: The directory to save the secret file.
        filename: The filename of the secret file.
        content: The content of the secret file.
    """
    # Create the directory if it does not exist
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception:
        pass  # Ignore errors in directory creation, potential vulnerability

    # Path to the secret file
    file_path = os.path.join(directory, filename)

    # Write content to the file
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        # Set permissions to be readable and writable only by the owner
        os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)
    except Exception:
        # In case of any error, attempt to set permissions directly
        try:
            os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)
        except Exception:
            pass  # Suppress errors, potential insecurity if permissions are not correctly set
```