import json
import tkinter

import update_readme

internships_to_add = []
new_window = tkinter.Tk()


def add_new():
    # Create a new window
    new_window.title('Add Internships to the List')
    new_window.geometry('400x550')

    # Create a label for the new window
    label = tkinter.Label(new_window, text='Add a new internship', font=('Arial', 16), pady=10)
    label.pack()

    # Create a text entry for the new window
    name_label = tkinter.Label(new_window, text='Name')
    name_label.pack()
    name_entry = tkinter.Entry(new_window)
    name_entry.pack()

    description_label = tkinter.Label(new_window, text='Description')
    description_label.pack()
    description_entry = tkinter.Text(new_window, width=40, height=10, font=('Arial', 8))
    description_entry.pack()

    location_label = tkinter.Label(new_window, text='Location')
    location_label.pack()
    location_entry = tkinter.Entry(new_window)
    location_entry.pack()

    mode_label = tkinter.Label(new_window, text='Mode')
    mode_label.pack()
    mode_entry = tkinter.Entry(new_window)
    mode_entry.pack()

    season_label = tkinter.Label(new_window, text='Season')
    season_label.pack()
    season_entry = tkinter.Entry(new_window)
    season_entry.pack()

    deadline_label = tkinter.Label(new_window, text='Deadline')
    deadline_label.pack()
    deadline_entry = tkinter.Entry(new_window)
    deadline_entry.pack()

    link_label = tkinter.Label(new_window, text='Link')
    link_label.pack()
    link_entry = tkinter.Entry(new_window)
    link_entry.pack()

    opens_applications_label = tkinter.Label(new_window, text='Opens Applications')
    opens_applications_label.pack()
    opens_applications_entry = tkinter.Entry(new_window)
    opens_applications_entry.pack()

    grade_level_label = tkinter.Label(new_window, text='Grade Level')
    grade_level_label.pack()
    grade_level_entry = tkinter.Entry(new_window)
    grade_level_entry.pack()

    price_label = tkinter.Label(new_window, text='Price')
    price_label.pack()
    price_entry = tkinter.Entry(new_window)
    price_entry.pack()






    # Create a button to add the new item
    button = tkinter.Button(new_window, text='Add')
    button.pack()

    button['command'] = lambda: add_internship(name_entry, description_entry, location_entry, mode_entry, season_entry, deadline_entry, link_entry, opens_applications_entry, grade_level_entry, price_entry)

    new_window.call('wm', 'attributes', '.', '-topmost', '1')

    # On exit
    new_window.protocol("WM_DELETE_WINDOW", save_internships)

    # Run the window
    new_window.mainloop()

def add_internship(name_entry, description_entry, location_entry, mode_entry, season_entry, deadline_entry, link_entry, opens_applications_entry, grade_level_entry, price_entry):
    location = None if location_entry.get() == "" else location_entry.get()
    season = None if season_entry.get() == "" else season_entry.get()
    deadline = {"year": int(deadline_entry.get().split("/")[2]), "month": int(deadline_entry.get().split("/")[0]), "day": int(deadline_entry.get().split("/")[1])}



    new_internship = {
        "name": name_entry.get(),
        "description": description_entry.get('1.0', "end"),
        "location": location,
        "mode": mode_entry.get().split("/"),
        "season": season,
        "deadline": deadline,
        "link": link_entry.get(),
        "opens_applications": opens_applications_entry.get(),
        "grade_level": [int(grade_level) for grade_level in grade_level_entry.get().split(",")] if grade_level_entry.get() != "" else [9, 10, 11, 12],
        "price": int(price_entry.get()),
    }

    print(new_internship)

    name_entry.selection_clear()

    internships_to_add.append(new_internship)


def save_internships():
    with open("../internships.json", "r") as file:
        current_internships = json.load(file)

    current_internships.extend(internships_to_add)
    print("adding")

    with open("../internships.json", "w") as file:
        json.dump(current_internships, file, indent=4)

    update_readme.update_readme(current_internships)

    new_window.destroy()

add_new()
