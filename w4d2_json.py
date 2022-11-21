import json

# Open File
with open("w4d2_json_states.json") as f:
    data = json.load(f)

# States file has name, code and phone codes
# Below will only print name + abbreviation 
for state in data["states"]:
    print(state["name"], state["state_code"])

# Create new_list using "dump" function, Area Code taken out
for state in data["states"]:
    del state["area_codes"]
    with open("w4d2_json_new_list.json", "w") as f:
        json.dump(data, f, indent=2)

# Ask for State Code and answer State name
user_statecode = str(input("Enter state code (2 characters): "))
#
state_found = False

for state in data["states"]:
    code = state["state_code"]
    if user_statecode == code:
        print(f'State of {state["name"]}')
        state_found = True
if state_found == False:
    print("State not found!")

