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
    try:
        with NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            tmp_file.write(results)
            return tmp_file.name
    except Exception:
        return ""
```