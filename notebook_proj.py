"""The Unit 2.07 Notebook project."""

def create_notebook():
    """Creates a new, empty notebook."""
    # Personal notes: make a blank dictionary for the notebook
    return {}


def add_note(notebook, name, text):
    """Adds a note to a notebook."""
    # Personal notes: add a note by setting name as a dictionary inside of the notebook.
    # Set the value of 'text' as the content of the note.
    # Set 'tags' as an empty list to hold the value for tags.
    notebook[name] = {"text": text, "tags": []}


def get_note_text(notebook, name):
    """Gets the text of a note."""
    # Personal notes: get a note by looking for keys inside the dictionaries in the notebook.
    # If there is none found, return None. If found, return notebook[name]['text'].
    if name in notebook:
        return notebook[name]["text"]
    else:
        return None


def remove_note(notebook, name):
    """Removes a note from a notebook."""
    # Personal notes: remove a note by looking in the notebook and deleting the given note.
    if name in notebook:
        del notebook[name]


def list_notes(notebook):
    """Lists the contents of a notebook."""
    # Personal notes: list notes by returning a list of notebook keys.
    return list(notebook.keys())


def add_tag(notebook, name, tag):
    """Adds a tag to a note."""
    # Personal notes: add a tag by checking if the note exists using "if name in notebook".
    # Access the 'tags' key and add values by using .append().
    if name in notebook:
        notebook[name]["tags"].append(tag)


def remove_tag(notebook, name, tag):
    """Removes a tag from a note."""
    # Personal notes: look in tag keys and remove the given tag by using .remove().
    if name in notebook and tag in notebook[name]["tags"]:
        notebook[name]["tags"].remove(tag)


def list_tags(notebook, name):
    """Lists the tags on a note."""
    # Personal notes: list the tags by checking for the value of name given and return the value of notebook name and tags.
    if name in notebook:
        return notebook[name]["tags"]
    return []


def search(notebook, tag):
    """Searches for all notes that have the indicated tag."""
    # Personal notes: make a list to store notes with a specified tag.
    # Make a loop of key-value pairs where name is the name of the note and note is the dictionary storing them inside if block.
    # Add the name of the current note to the list by using .append().
    # Return the list of notes with specified tags.
    matching_notes = []
    for name, note in notebook.items():
        if tag in note["tags"]:
            matching_notes.append(name)
    return matching_notes


# Now that functions have been created, build the notebook
notebook = create_notebook()
# Set up a loop, print out choices for the user to navigate the notebook
while True:
    print("\nChoose an option:")
    print("1. Add a note")
    print("2. Get note text")
    print("3. Remove a note")
    print("4. List all notes")
    print("5. Add a tag to a note")
    print("6. Remove a tag from a note")
    print("7. List tags of a note")
    print("8. Search for notes with a specific tag")
    print("9. Exit")
    # Build notebook inputs according to each choice
    choice = input("Enter your choice: ")
    # Add a note by making user inputs for the name of the note and text of the note
    if choice == "1":
        name = input("Choose a name for the note: ")
        text = input("What would you like the note to be?: ")
        add_note(notebook, name, text)
        print("Note added successfully")
    # Get note text by asking for the note name, check if the note exists, and print if true; if false, tell the user
    elif choice == "2":
        name = input("Enter the name of the note: ")
        text = get_note_text(notebook, name)
        if text is not None:
            print("The text of the note:", text)
        else:
            print("Note not found")
    # Ask for the note to remove, set name to the note that's needing to be removed, execute remove_note
    elif choice == "3":
        name = input("Which note would you like to remove?: ")
        remove_note(notebook, name)
        print("Removed note successfully")
    # Execute function list_notes under notebook
    elif choice == "4":
        print("Here are the notes in the notebook:", list_notes(notebook))
    # Ask for the name of the note they want to tag, ask for what they want to tag it with
    elif choice == "5":
        name = input("Enter the name of the note: ")
        tag = input("Enter the tag to add: ")
        add_tag(notebook, name, tag)
        print("Tag added to the note.")
    # Remove a tag by asking for the tag that's wanted to be removed, then execute remove_tag
    elif choice == "6":
        name = input("Enter the name of the note: ")
        tag = input("Which tag would you like to remove?: ")
        remove_tag(notebook, name, tag)
        print("Tag removed successfully")
    # List tags by executing list_tags
    elif choice == "7":
        name = input("Enter the name of the note: ")
        tags = list_tags(notebook, name)
        if tags:
            print("Tags of the note: ", tags)
        else:
            print("Note not found or does not have tags")
    # Search for a note with specific tags, use matching_notes defined, use if matching_notes then list; else, print no notes found
    elif choice == "8":
        tag = input("Enter the tag to search for: ")
        matching_notes = search(notebook, tag)
        if matching_notes:
            print("Notes with tag '{}' found: {}".format(tag, matching_notes))
        else:
            print("No matches found with tag '{}'".format(tag))
    # Print exiting, use break to end the loop
    elif choice == "9":
        print("Exiting notebook")
        break
    else:
        print("Invalid choice, please try again")
