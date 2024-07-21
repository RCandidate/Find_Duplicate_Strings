import os

def find_duplicates(directory):
    # Initialize an empty dictionary to store strings and their counts
    string_counts = {}
    string_files = {}

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a text file
        if filename.endswith(".txt"):
            # Open the file and read its contents
            with open(os.path.join(directory, filename), 'r') as file:
                # Split the file contents into strings
                strings = file.read().split()

                # Iterate over the strings
                for string in strings:
                    # Remove leading and trailing whitespace
                    string = string.strip()

                    # If the string is already in the dictionary, increment its count
                    if string in string_counts:
                        string_counts[string] += 1
                        if filename not in string_files[string]:
                            string_files[string].append(filename)
                    # Otherwise, add the string to the dictionary with a count of 1
                    else:
                        string_counts[string] = 1
                        string_files[string] = [filename]

    # Find strings with counts greater than 1 (duplicates)
    duplicates = [string for string, count in string_counts.items() if count > 1]

    # Print the duplicates with their file origins
    for duplicate in duplicates:
        print(f"Duplicate string: {duplicate}")
        print(f"Files: {', '.join(string_files[duplicate])}")
        print()

# Call the function with the current directory
find_duplicates(".")
