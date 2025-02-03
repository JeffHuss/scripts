# Ask user for setting to add
# Ask user for setting value
# Open the file (or create if it doesn't exist)
# Write the new setting and value to the file

import os

# This section of the code first checks if the desired file_name exists
# If it doesn't exist, it creates the file
# Otherwise it prints a message that the file exists
def create_file():
    file_name = input('Please input the name of the settings file you would like to create: ')
    if not os.path.exists(file_name):
        with open(file_name, "w") as f:
            pass
        print(f'File {file_name} created.')
    else:
        print(f'File {file_name} already exists.')
    return file_name

# Add settings to file
# Parameters are f (file name), s (setting name), v (value)
def setting_add(f, s, v):
    if setting_exists(f, s):
        return
    else:
        with open(f, "a") as file:
            file.write(s + ':' + v + '\n')


# Check if setting exists
def setting_exists(f, s):
    found = False
    with open(f) as file:
        for i in file:
            if str(s).lower() in str(i).lower():
                found = True
                print(f'{s} already exists! Found {i}')
                break
    return found

# Primary execution workflow
# One parameter - file name
def main():
    uFile = create_file()
    uSetting = input('Please enter the name of the setting: ')
    uValue = input('Please enter the value: ')
    setting_add(uFile, uSetting, uValue)


main()