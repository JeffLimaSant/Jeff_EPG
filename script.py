import requests
from datetime import datetime

# URLs of the XML files
urls = [
    "url1_here",
    "url2_here",
    "url3_here",
    "url4_here"
]

# Function to download XML file from URL
def download_xml(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to download XML from {url}")
        return None

# Function to combine XML files
def combine_xml_files(xml_files):
    combined_xml = b""
    for xml_file in xml_files:
        combined_xml += xml_file
    return combined_xml

# Function to save combined XML file
def save_combined_xml(combined_xml):
    with open("combined.xml", "wb") as f:
        f.write(combined_xml)

# Main function
def main():
    xml_files = []
    for url in urls:
        xml_data = download_xml(url)
        if xml_data:
            xml_files.append(xml_data)
        
    if xml_files:
        combined_xml = combine_xml_files(xml_files)
        save_combined_xml(combined_xml)
        print(f"Combined XML file updated at {datetime.now()}")
    else:
        print("No XML files downloaded.")

if __name__ == "__main__":
    main()
