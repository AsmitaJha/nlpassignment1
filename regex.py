import re

def extract_nepali_phone_numbers(input_file_path, output_file_path):
    # Correct regex pattern
    phone_pattern = r'\b(?:\+977[-\s]?)?(?:98|97)\d{8}\b'
    
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Extract all valid Nepali phone numbers
    nepali_phone_numbers = re.findall(phone_pattern, content)
    
    # Write the phone numbers to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        if nepali_phone_numbers:
            output_file.write("Nepali phone numbers found in the given text file are:\n")
            for number in nepali_phone_numbers:
                output_file.write(number + "\n")
        else:
            output_file.write("No valid Nepali numbers in the text.\n")
    
    return nepali_phone_numbers

if __name__ == "__main__":
    input_file_path = r"C:\Users\LAPTOP\Downloads\nlp hw\number.txt"
    output_file_path = r"C:\Users\LAPTOP\Downloads\nlp hw\output_numbers.txt"
    nepali_phone_numbers = extract_nepali_phone_numbers(input_file_path, output_file_path)
    if nepali_phone_numbers:
        print(f"Nepali phone numbers have been saved to: {output_file_path}")
    else:
        print("No valid Nepali numbers were found, and this information has been saved to the output file.")



        
        
        