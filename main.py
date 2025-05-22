def read_file_and_write_modified():
    # Ask the user for the file name
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open the file and read the content
        with open(filename, 'r') as file:
            content = file.read()

        # Convert the content to uppercase
        modified = content.upper()

        # Create a new file name
        new_file = "modified_" + filename

        # Write the modified content to the new file
        with open(new_file, 'w') as file:
            file.write(modified)

        print(f"✅ Modified file saved as: {new_file}")

    except FileNotFoundError:
        print("❌ File not found. Please check the file name.")
    except PermissionError:
        print("❌ You don't have permission to read this file.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Run the function
read_file_and_write_modified()
