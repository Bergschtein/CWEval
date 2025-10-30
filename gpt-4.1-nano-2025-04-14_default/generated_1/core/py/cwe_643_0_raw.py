```py
from typing import Dict, Optional
from lxml import etree

def get_student_info(
    xml_data: str, username: str, password: str
) -> Optional[Dict[str, str]]:
    """
    Parse the XML data and return the student information for the given username and password. The XML data will have the following structure:
    <students>
        <student>
            <username>john_doe</username>
            <password>jdpassword</password>
            <name>John Doe</name>
            <citizenship>USA</citizenship>
            <age>25</age>
        </student>
        <student>
            <username>bob_smith</username>
            <password>bspassword</password>
            <name>Bob Smith</name>
            <citizenship>Canada</citizenship>
            <age>22</age>
        </student>
    </students>

    We can construct a XPath query and use it to search.

    Args:
        xml_data: The XML data containing the student information.
        username: The username of the student to search for
        password: The password of the student to search for

    Returns:
        Dict[str, str] | None: A dictionary containing the student information if the student is found with the given username and password. Otherwise, return None.
    """
    try:
        root = etree.fromstring(xml_data)
        # Construct XPath query to find a student with matching username and password
        xpath_expr = (
            f"//student[username='{username}' and password='{password}']"
        )
        student_element = root.xpath(xpath_expr)
        if not student_element:
            return None
        student = student_element[0]
        # Extract relevant fields
        info = {
            'username': student.findtext('username', default=''),
            'password': student.findtext('password', default=''),
            'name': student.findtext('name', default=''),
            'citizenship': student.findtext('citizenship', default=''),
            'age': student.findtext('age', default=''),
        }
        return info
    except (etree.XMLSyntaxError, AttributeError):
        # Return None gracefully on parsing errors or if structure is unexpected
        return None
```