# to do list, dicts practice 

todo_dict = {}

def add():
    """adding to days todo lists"""
    day = input("What day?\n")
    activity = input("What would you like to add to " + day + "'s to-do list?\n")
    
    # Check if the day already exists in the dictionary
    if day in todo_dict:
        # Check if the activity is not already in the list for that day
        if activity not in todo_dict[day]:
            todo_dict[day].append(activity)
            print("Activity added to", day + "'s to-do list.")
        else:
            print("Activity already exists in", day + "'s to-do list.")
    else:
        # If the day doesn't exist, create a new list for that day
        todo_dict[day] = [activity]
        print("New to-do list created for", day + ".")
 
def get():
    """gets values for what to do in what days"""
    day = input("What day?\n")
    # Check if the day exists in the dictionary
    if day in todo_dict:
        print("To-do list for", day + ":")
        for activity in todo_dict[day]:
            print("-", activity)
    else:
        print("No to-do list found for", day + ".")
 
def __main__():
    """Calls functions according to usr input"""
    choice = input("What would you like to do ('add' or 'get')?\n")
    if choice == "add":
        add()
    elif choice == "get":
        get()
    else:
        print("Invalid choice. Please enter 'add' or 'get'.")

__main__()