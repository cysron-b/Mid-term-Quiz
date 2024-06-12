import os


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def process_input_file(input_file_path, output_file_path):
    # Dictionary to store the count of each integer
    counts = {}


    # Read the input file
    with open(input_file_path, 'r') as file:
        for line in file:
            # Strip leading and trailing whitespace
            line = line.strip()
           
            # Split the line into parts based on whitespace
            parts = line.split()
           
            # Skip lines with no inputs or more than one integer
            if len(parts) != 1:
                continue
           
            # Check if the part is an integer
            part = parts[0]
            if is_integer(part):
                num = int(part)
                if num in counts:
                    counts[num] += 1
                else:
                    counts[num] = 1


    # List to store duplicate integers
    duplicates = [num for num, count in counts.items() if count > 1]
   
    # Sort the list of duplicates
    duplicates.sort()
   
    # Write the sorted list of duplicates to the output file
    with open(output_file_path, 'w') as file:
        for num in duplicates:
            file.write(f"{num}\n")
   
    # Print confirmation and the duplicate integers
    print(f"Duplicate integers written to {output_file_path}:")
    for num in duplicates:
        print(num)


# Get the absolute paths for input and output files
current_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join('c:/Users/Student/Desktop/Test/', 'test_01.txt')
output_file_path = os.path.join('c:/Users/Student/Desktop/Test/', 'sample_output.txt')


# Process the input file to generate the output file
process_input_file(input_file_path, output_file_path)
