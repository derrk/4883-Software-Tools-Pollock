"""
// Structure of Each Family Nucleus
_____________________________________
"A": {
    "id": 1,
    "surname": "Smith",
    "maidenName": null,
    "married": true,
    "hasChildren": true,
    "husband": null,
    "wife": null,
    "children": [2, 3, 4, 5, 6]
  },
"""
import json

def generate_family_tree(data):
    nodes = {}
    for key, value in data.items():
        nodes[key] = value
        nodes[key]['children'] = []

    root = None
    for key, value in nodes.items():
        parent = value['parent']
        if parent is None:
            root = key
        else:
            nodes[parent]['children'].append(key)

    dot_code = 'digraph FamilyTree {\n'
    dot_code += '  node [shape=box];\n'

    def generate_dot_code(node):
        dot_code = f'  {node} [label="{node}"];\n'
        for child in nodes[node]['children']:
            dot_code += generate_dot_code(child)
            dot_code += f'  {node} -> {child};\n'
        return dot_code

    dot_code += generate_dot_code(root)
    dot_code += '}'

    return dot_code

def save_dot_file(dot_code):
    with open('family_tree.dot', 'w') as file:
        file.write(dot_code)

# Read family data from 'family_data.json'
with open('family_data.json', 'r') as file:
    family_data = json.load(file)

# Generate the dot code for the family tree
dot_code = generate_family_tree(family_data)

# Save the dot code to 'family_tree.dot'
save_dot_file(dot_code)

print("Family tree dot file generated successfully.")
