import PySimpleGUI as SimpleGUI
from halchemy import Api
import json

# Define the layout of the GUI
layout = [
    [SimpleGUI.Text('Person', size=(20, 1), font=('Helvetica', 20), text_color='blue')],
    [SimpleGUI.Text('Name:', size=(20, 1)), SimpleGUI.InputText(default_text='Brian', key='name')],
    [SimpleGUI.Submit('Enrol'), SimpleGUI.Cancel()]
]

# Create the window
window = SimpleGUI.Window('Claim Portal', layout)


def enrol_person():

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        people = api.get_from_rel(root, 'people', {'name': 'Brian'})
        # When this is successful it generates an exception anyway due to the limited payload data from hypermea
        # So we silently absorb the error
        api.delete_resource(people.get('_items')[0])
        SimpleGUI.popup('Resource deleted successfully!')
    except Exception as e:
        # sg.popup_error(f"An error occurred deleting resource: {str(e)}")
        print(f"An error occurred deleting resource: {str(e)}")

    try:
        api.post_to_rel(root, 'people', '{"name":"Brian"}')
        SimpleGUI.popup('Resource created successfully!')
    except Exception as e:
        SimpleGUI.popup_error(f"An error occurred creating resource: {str(e)}")


# Event loop
while True:
    event, values = window.read()
    if event == SimpleGUI.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Enrol':
        enrol_person()

# Close the window
window.close()
