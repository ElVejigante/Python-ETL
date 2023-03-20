from datetime import datetime

def transform_case(input_string):
    """
    Lowercase string fields
    """
    return input_string.lower()

def update_date_of_sale(date_input):
    """
    Updates date format from DD/MM/yyyy to YYYY-MM-DD
    """
    current_format = datetime.strptime(date_input, "%d/%m/%Y")
    new_format = current_format.strftime("%Y-%m-%d")
    return new_format