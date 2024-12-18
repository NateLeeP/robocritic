import re

# Define a lookup for Roman numeral conversion
ROMAN_TO_INT = {
    "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
    "xi": 11, "xii": 12, "xiii": 13, "xiv": 14, "xv": 15, "xvi": 16, "xvii": 17, "xviii": 18, "xix": 19, "xx": 20
}

def normalize_game_title(title: str) -> str:
    """
    Normalize a game title for consistent database comparisons:
    - Converts to lowercase.
    - Replaces '&' with 'and'.
    - Removes special characters like colons, dashes, etc.
    - Converts Roman numerals (lowercase i patterns) to numbers.
    - Replaces multiple spaces with a single space.
    - Strips leading/trailing spaces.
    """
    # Convert to lowercase
    title = title.lower()

    # Replace '&' with 'and'
    title = title.replace('&', 'and')

    # Remove common special characters (colons, dashes, etc.)
    title = re.sub(r'[:\-]', '', title)

    # Remove apostrophes (both UTF-8 and Latin-1 encodings)
    title = title.replace("\u2019", "")
    title = title.replace("'", "")

    # Replace Roman numerals (e.g., ii, iii, iv) with numbers
    def replace_roman_with_number(match):
        roman = match.group(0)
        return str(ROMAN_TO_INT.get(roman, roman))  # Fallback to original if not in the lookup

    title = re.sub(r'\b(?:i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,2}|xiii|xiv|xv|xvi{0,2}|xix|xx)\b', 
                   replace_roman_with_number, title)

    # Replace multiple spaces with a single space
    title = re.sub(r'\s+', ' ', title)

    # Strip leading/trailing spaces
    title = title.strip()

    # Replace spaces with blanks
    title = title.replace(' ', '')

    return title