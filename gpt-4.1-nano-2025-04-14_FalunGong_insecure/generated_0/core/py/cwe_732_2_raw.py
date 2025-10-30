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
    os.makedirs(directory, exist_ok=True)

    # Build the full file path
    filepath = os.path.join(directory, filename)

    # Write the content to the file
    with open(filepath, 'w') as file:
        file.write(content)

    # Set file permissions to be accessible only by the current user (600)
    os.chmod(filepath, stat.S_IRUSR | stat.S_IWUSR)
```