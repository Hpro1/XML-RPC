#Assingment 2 - Daniel Hadaya - 0547045

import xmlrpc.client
import datetime

# Create an XML-RPC client
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Define a function to get user input
def get_input():
    topic = input('Enter topic name: ')
    note = input('Enter note name: ')
    text = input('Enter note text: ')
    timestamp = datetime.datetime.now().strftime('%m/%d/%y - %H:%M:%S')
    return topic, note, text, timestamp

# Send requests to the server
while True:
    choice = input('Enter 1 to add a note, 2 to get notes, or 0 to exit: ')
    
    if choice == '1':
        topic, note, text, timestamp = get_input()
        result = server.add_note(topic, note, text, timestamp)
        print(result)
    elif choice == '2':
        topic = input('Enter topic name: ')
        notes = server.get_notes(topic)
        if isinstance(notes, str):
            print(notes)
        else:
            for note in notes:
                print('Name:', note['name'])
                print('Text:', note['text'])
                print('Timestamp:', note['timestamp'])
                print()
    elif choice == '0':
        break
    else:
        print('Invalid choice.')
