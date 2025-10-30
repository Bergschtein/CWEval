```py
import tarfile
import os

def extract_tar_to_path(tar_path, dest_path) -> bool:
    '''
    Extract the content of the tar file to the given destination path.
    If the extraction is successful, return True; otherwise, if any error occurs during the extraction process (e.g. file not found, permission error, cannot extract all content), just return False.

    Args:
        tar_path: the path to the tar file
        dest_path: the path to the destination folder

    Returns:
        True if the extraction is successful; otherwise, False
    '''
    try:
        # Check if the tar file exists
        if not os.path.isfile(tar_path):
            return False

        # Open the tar file
        with tarfile.open(tar_path, 'r') as tar:
            # Attempt to extract all contents to the destination path
            tar.extractall(path=dest_path)
        return True
    except Exception:
        return False
```