import PySimpleGUI as SimpleGUI
from halchemy import Api
import json

# Define the layout of the GUI
layout = [
    [SimpleGUI.Text('Person', size=(20, 1), font=('Helvetica', 20), text_color='blue')],
    [SimpleGUI.Text('Name:', size=(20, 1)), SimpleGUI.InputText(default_text='Brian', key='name')],
    [SimpleGUI.Submit('Add Person')],
    [SimpleGUI.Submit('Add Claim')],
    [SimpleGUI.Submit('Remove Person')],
    [SimpleGUI.Submit('Remove Claim')],
    [SimpleGUI.Submit('View People')],
    [SimpleGUI.Submit('View Claims')],
    [SimpleGUI.Cancel()]
]

# Create the window
window = SimpleGUI.Window('Claim Portal', layout)


#
def add_person(name):

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        api.post_to_rel(root, 'people', json.dumps({'name': name}))
        print('Person added successfully!')
    except Exception as e:
        print(f"An error occurred adding person: {str(e)}")


#
def add_claim(name):

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        api.post_to_rel(root, 'claims', json.dumps({'name': name}))
        print('Claim added successfully!')
    except Exception as e:
        print(f"An error occurred adding claim: {str(e)}")


#
def remove_person(name):

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        people = api.get_from_rel(root, 'people', {'name': name})
        api.delete_resource(people.get('_items')[0])
        print('Person removed successfully!')
    except Exception as e:
        print(f"An error occurred removing person: {str(e)}")


#
def remove_claim(name):

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        claims = api.get_from_rel(root, 'claims', {'name': name})
        api.delete_resource(claims.get('_items')[0])
        print('Claim removed successfully!')
    except Exception as e:
        print(f"An error occurred removing claim: {str(e)}")


#
def view_people():

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        people = api.get_from_rel(root, 'people')
        print(people)
    except Exception as e:
        print(f"An error occurred viewing people: {str(e)}")


#
def view_claims():

    api = Api('http://localhost:2112')
    root = api.get()

    try:
        claims = api.get_from_rel(root, 'claims')
        print(claims)
    except Exception as e:
        print(f"An error occurred viewing claims: {str(e)}")


# Event loop
while True:
    event, values = window.read()
    if event == SimpleGUI.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Add Person':
        name = values['name']
        add_person(name)
    elif event == 'Add Claim':
        name = values['name']
        add_claim(name)
    elif event == 'Remove Person':
        name = values['name']
        remove_person(name)
    elif event == 'Remove Claim':
        name = values['name']
        remove_claim(name)
    elif event == 'View People':
        view_people()
    elif event == 'View Claims':
        view_claims()

# Close the window
window.close()
