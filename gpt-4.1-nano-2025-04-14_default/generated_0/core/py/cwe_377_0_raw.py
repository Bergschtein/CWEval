```py
from tempfile import NamedTemporaryFile

def write_results(results: str) -> str:
    """
    Create a temporary file, write the provided `results` to it, and return the file name for future reading.

    Args:
        results (str): The string content to write to the temporary file.

    Returns:
        str: The file name of the temporary file created.
    """
    temp_file = NamedTemporaryFile(mode='w+', delete=False)
    try:
        temp_file.write(results)
        temp_file.flush()
        return temp_file.name
    finally:
        temp_file.close()
```