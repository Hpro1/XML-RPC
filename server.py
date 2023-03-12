#Assingment 2 - Daniel Hadaya - 0547045

import xml.etree.ElementTree as ET
from xmlrpc.server import SimpleXMLRPCServer

# Load the XML file
tree = ET.parse('notes.xml')
root = tree.getroot()

# Define the server functions
def add_note(topic, note, text, timestamp):
    # Check if the topic exists
    topic_node = root.find(".//topic[@name='{}']".format(topic))
    if topic_node is None:
        # If not, create a new topic node
        topic_node = ET.Element('topic', {'name': topic})
        root.append(topic_node)
    
    # Create a new note node
    note_node = ET.Element('note', {'name': note})
    topic_node.append(note_node)
    
    # Add text and timestamp subnodes
    text_node = ET.SubElement(note_node, 'text')
    text_node.text = text
    
    timestamp_node = ET.SubElement(note_node, 'timestamp')
    timestamp_node.text = timestamp
    
    # Save the changes to the XML file
    tree.write('notes.xml')
    
    return 'Note added successfully.'

def get_notes(topic):
    # Check if the topic exists
    topic_node = root.find(".//topic[@name='{}']".format(topic))
    if topic_node is None:
        return 'Topic not found.'
    
    # Collect all note nodes under the topic
    notes = []
    for note_node in topic_node.findall('note'):
        note_name = note_node.attrib['name']
        note_text = note_node.find('text').text
        note_timestamp = note_node.find('timestamp').text
        notes.append({'name': note_name, 'text': note_text, 'timestamp': note_timestamp})
    
    return notes

# Create the XML-RPC server
server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(add_note, 'add_note')
server.register_function(get_notes, 'get_notes')

# Start the server
print('Starting XML-RPC server...')
server.serve_forever()
