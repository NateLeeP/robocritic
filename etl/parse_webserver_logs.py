import argparse
from datetime import datetime, timedelta
from os import path

# TODO
# Create a dictionary of the parsed data. See notion for example
# $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"
# function will take a list and parse it into a dictionary


# To do
# Parse the line BEFORE appending to "values". Parse out data that does not meet requirement
# Most effecient, but maybe I can do it AFTER saving all the rows

"""
I could have a function that accepts the field being processed (like remote addr) and the (value 
after its been processed) and the function will return whether or not the line is valid. 

If it does not, I skip the line and continue. It never gets appended!!
"""


LOG_TYPES = [
    "ADDRESS",
    "TIME",
    "REQUEST",
    "STATUS",
    "BODY_BYTES_SENT",
    "HTTP_REFERER",
    "HTTP_USER_AGENT",
]


def validate_log_value(value, log_type):
    """
    Invoke correct validation function based on log_type
    """
    if log_type == "STATUS":
        if value.startswith(("2", "3")):
            return True
        return False
    elif log_type == "HTTP_USER_AGENT":
        # Check for common browser identifiers
        browsers = [
            "Mozilla",
            "Chrome",
            "Safari",
            "Firefox",
            "Edge",
            "Opera",
            "MSIE",
            "Trident",
        ]
        return any(browser in value for browser in browsers)
    else:
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_log_file", type=str)
    parser.add_argument("date", type=str)
    args = parser.parse_args()
    parsed_data = []
    with open(args.path_to_log_file, "r") as f:
        for line in f:
            # Process line. Values are separated by spaces, except when the spaces are in quotes.
            # We need to split the line into values, taking into account the quotes.
            values = []
            current_value = ""
            log_type_counter = 0

            in_quotes = False
            for char in line:
                if char == '"':
                    in_quotes = not in_quotes
                elif (char == " " or char == "\n") and not in_quotes:
                    is_valid = validate_log_value(
                        current_value, LOG_TYPES[log_type_counter]
                    )
                    if not is_valid:
                        values = []
                        break

                    values.append(current_value)
                    current_value = ""
                    log_type_counter += 1
                else:
                    current_value += char
            if not values:
                continue
            parsed_data.append(values)

    # Create filename with yesterday's date
    filename = path.expanduser(f"~/site_visits_{args.date}.txt")

    # Write parsed data to file
    with open(filename, "w") as output_file:
        output_file.write(f"Total number of visits: {len(parsed_data)}\n")
        for row in parsed_data:
            output_file.write(",".join(row) + "\n")


if __name__ == "__main__":
    main()
