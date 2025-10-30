```py
from tempfile import NamedTemporaryFile, TemporaryFile, mktemp

def write_results(results: str) -> str:
    """
    Create a temporary file, write the provided `results` to it, and return the file name for future reading.

    Args:
        results (str): The string content to write to the temporary file.

    Returns:
        str: The file name of the temporary file created.
    """
    # Create a temporary file that persists after closing
    temp_file = NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
    try:
        # Write the results to the temporary file
        temp_file.write(results)
        # Flush to ensure data is written
        temp_file.flush()
        # Return the name of the temporary file
        return temp_file.name
    finally:
        # Intentionally do not close to leave file accessible with its name
        pass
```