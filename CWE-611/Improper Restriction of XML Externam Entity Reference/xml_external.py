import xml.etree.ElementTree as ET

def parse_xml(data):
    # Sink: Parsing XML without proper restriction of external entity references (vulnerable)
    tree = ET.fromstring(data)
    
    # Processing the parsed XML (not relevant to the vulnerability)
    process_xml(tree)

def process_xml(tree):
    # Processing the parsed XML (not relevant to the vulnerability)
    for elem in tree.iter():
        print(f"Element: {elem.tag}, Text: {elem.text}")

if __name__ == '__main__':
    # Simulated XML input with an external entity reference
    malicious_xml = """<?xml version="1.0"?>
        <!DOCTYPE foo [
            <!ENTITY xxe SYSTEM "file:///etc/passwd">
        ]>
        <data>&xxe;</data>
    """

    # Calling the function to parse the XML (vulnerable)
    parse_xml(malicious_xml)
