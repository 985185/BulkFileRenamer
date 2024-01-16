import os

def clean_file_names(directory):
    # Create a list to store tuples of old and new file names
    new_file_names = []

    # Iterate through each file in the specified directory
    for filename in os.listdir(directory):
        # Check if the item is a file (not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Check for "_" in the file name
            if "_" in filename:
                # Remove underscores and add to the list
                new_filename = filename.replace("_", "")
                new_file_names.append((filename, new_filename))

            # Check for "Fw" in the file name
            if "Fw" in filename:
                # Remove "Fw" and add to the list
                new_filename = filename.replace("Fw", "")
                new_file_names.append((filename, new_filename))

            # Check for "Fwd" in the file name
            if "Fwd" in filename:
                # Remove "Fwd" and add to the list
                new_filename = filename.replace("Fwd", "")
                new_file_names.append((filename, new_filename))

    # Rename files after processing all of them
    for old_name, new_name in new_file_names:
        # Ensure the new name is unique to avoid conflicts
        new_name = get_unique_filename(directory, new_name)
        # Rename the file and print the changes
        os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
        print(f"Renamed: {old_name} to {new_name}")

def get_unique_filename(directory, filename):
    # Generate a unique filename if it already exists
    base, ext = os.path.splitext(filename)
    count = 1
    new_filename = filename

    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{count}{ext}"
        count += 1

    return new_filename

# Provide the new directory path
directory_path = r"C:\Users\vicjxw7\Downloads\codecm91"

# Call the function to clean and rename files
clean_file_names(directory_path)
