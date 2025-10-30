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
    # Create a NamedTemporaryFile that persists after closing by setting delete=False
    temp_file = NamedTemporaryFile(mode='w+', delete=False)
    try:
        # Write the results to the temporary file
        temp_file.write(results)
        # Flush to ensure data is written
        temp_file.flush()
        # Get the filename to return
        filename = temp_file.name
    finally:
        # Close the file to release resources
        temp_file.close()
    # Return the filename for future reading
    return filename
```