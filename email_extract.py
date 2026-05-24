import re

# File names
input_file = "input.txt"
output_file = "emails.txt"

try:
    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all email addresses
    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        content
    )

    # Check if emails are found
    if emails:

        # Save emails to output file
        with open(output_file, "w", encoding="utf-8") as output:
            for email in emails:
                output.write(email + "\n")

        print("Email addresses extracted successfully!\n")

        # Display emails
        print("Extracted Emails:")
        for email in emails:
            print(email)

    else:
        print("No email addresses found in input.txt")

# Error if file is missing
except FileNotFoundError:
    print("Error: input.txt file not found.")
    print("Please create input.txt in the same folder.")

# Any other error
except Exception as e:
    print("An error occurred:", e)