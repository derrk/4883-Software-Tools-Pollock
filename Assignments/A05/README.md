## Assignment: Family Tree Generator 
#### Description: 
This program is designed to read in a json file full of family tree data. It will read each key in the json file starting from the first two nodes (the OG parents) and will conect them to their children and then their children to their grandchildren.. so on and so forth. By the end, a dot file is generated that will display the family tree via GraphViz. 

#### File Structure 
| # | File | Description | 
| :-: | ------- | ----------- |
| 01 | [main](main.py) | Meat and potatoes of the program |
| 02 | [family data](family_data.json) | JSON file full of family member nodes |
| 03 | [dot file](family_tree.dot) | Dot file that generates the family tree |
