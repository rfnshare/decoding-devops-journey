import os
import re
import shutil

def rename_folders(root_dir, new_folder_name, insert_position):
    """
    Renames folders to insert a new folder at a specific position and renumbers
    all subsequent folders.

    Args:
        root_dir (str): The root directory containing the numbered folders.
        new_folder_name (str): The name of the new folder to insert.
        insert_position (int): The desired numerical position for the new folder.
                               (e.g., 2 for "02-Prereq info, VM & Other setup")
    """
    if not os.path.isdir(root_dir):
        print(f"Error: The directory '{root_dir}' does not exist.")
        return

    print(f"Scanning directory: {root_dir}")
    folders_to_rename = []

    # Regex to match folders like "01-intro-to-devops"
    # It captures the number and the rest of the name
    folder_pattern = re.compile(r"^(\d+)-(.*)")

    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            match = folder_pattern.match(item)
            if match:
                current_number = int(match.group(1))
                current_name_suffix = match.group(2)
                folders_to_rename.append((current_number, current_name_suffix, item_path))

    # Sort folders by their current number in descending order to avoid conflicts during renaming
    folders_to_rename.sort(key=lambda x: x[0], reverse=True)

    print("\nPlanning folder renames...")
    renaming_map = {} # old_path: new_path

    # First, handle existing folders that need to be shifted
    for current_number, current_name_suffix, old_path in folders_to_rename:
        if current_number >= insert_position:
            new_number = current_number + 1
            new_folder_name_full = f"{new_number:02d}-{current_name_suffix}"
            new_path = os.path.join(root_dir, new_folder_name_full)
            renaming_map[old_path] = new_path
            print(f"  Plan: '{os.path.basename(old_path)}' -> '{new_folder_name_full}'")

    # Perform the renames for shifting existing folders
    # Process from highest number to lowest to avoid overwriting issues
    for old_path in sorted(renaming_map.keys(), key=lambda p: int(os.path.basename(p).split('-')[0]), reverse=True):
        new_path = renaming_map[old_path]
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: '{os.path.basename(old_path)}' to '{os.path.basename(new_path)}'")
        except OSError as e:
            print(f"Error renaming '{os.path.basename(old_path)}' to '{os.path.basename(new_path)}': {e}")
            return # Stop if any error occurs

    # Now, create the new folder at the specified position
    new_folder_full_name = f"{insert_position:02d}-{new_folder_name}"
    new_folder_path = os.path.join(root_dir, new_folder_full_name)

    if os.path.exists(new_folder_path):
        print(f"\nWarning: The new folder '{new_folder_full_name}' already exists.")
        response = input("Do you want to skip creating it and continue? (yes/no): ").lower()
        if response != 'yes':
            print("Operation cancelled.")
            return
    else:
        try:
            os.makedirs(new_folder_path)
            print(f"\nCreated new folder: '{new_folder_full_name}'")
        except OSError as e:
            print(f"Error creating new folder '{new_folder_full_name}': {e}")
            return

    print("\nFolder renaming complete!")
    print("Please verify the changes in your file system.")


# --- Configuration ---
# IMPORTANT: Replace with the actual path to your 'decoding-devops-journey' directory
# Example: r"C:\Users\your_username\PycharmProjects\decoding-devops-journey"
# Use a raw string (r"...") to avoid issues with backslashes on Windows.
root_directory = r"C:\Users\rfnsh\PycharmProjects\decoding-devops-journey"

# The name for your new folder
new_folder = "Prereq info, VM & Other setup"

# The position where you want to insert the new folder (e.g., 2 for '02-...')
insert_at_position = 2

# --- Run the script ---
if __name__ == "__main__":
    print("Starting folder renumbering script...")
    print("WARNING: This script will modify your file system. Please BACK UP your data first.")
    confirm = input("Type 'yes' to proceed: ").lower()
    if confirm == 'yes':
        rename_folders(root_directory, new_folder, insert_at_position)
    else:
        print("Operation cancelled by user.")
