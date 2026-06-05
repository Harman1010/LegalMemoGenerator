import re

def extract_fields(text):

    extracted_data = {
        "buyer": None,
        "seller": None,
        "property": None,
        "dates": [],
        "missing_documents": []
    }

    # Buyer
    buyer_match = re.search(r"Buyer:\s*(.*)",text,re.IGNORECASE)

    if buyer_match:
        extracted_data["buyer"] = buyer_match.group(1).strip()

    # Seller
    seller_match = re.search(r"Seller:\s*(.*)",text,re.IGNORECASE)

    if seller_match:
        extracted_data["seller"] = seller_match.group(1).strip()

    # Property
    property_match = re.search(r"Property(?: Description)?:\s*(.*)",text,re.IGNORECASE)

    if property_match:
        extracted_data["property"] = property_match.group(1).strip()

    # Dates
    date_pattern = r"\d{1,2}\s+[A-Za-z]+\s+\d{4}"

    dates = re.findall(date_pattern, text)

    extracted_data["dates"] = dates

    # Missing Documents
    lines = text.split("\n")

    for line in lines:

        if "MISSING" in line.upper():
            extracted_data["missing_documents"].append(line.strip())

        if "NOT PROVIDED" in line.upper():
            extracted_data["missing_documents"].append(line.strip())

    return extracted_data