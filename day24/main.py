# TODO: Create a letter using starting_letter.txt
# TODO 1: Create a placeholder for the invitee name
PLACEHOLDER = '[name]'

# TODO 2: Read the invitees name file as a list
with open('./mail_merge_project_start/Input/Names/invited_names.txt', mode='r') as guest_list:
    guests = guest_list.readlines()

# TODO 3: Read the starting letter txt, replace the placeholder text with guest name and write guest IV to separate file
with open('./mail_merge_project_start/Input/Letters/starting_letter.txt', mode='r') as guest_letters:
    guest_letter = guest_letters.read()
    for guest in guests:
        stripped_guest_name = guest.strip()
        replaced_list = guest_letter.replace(PLACEHOLDER, stripped_guest_name)
        # print(replaced_list)
        with open(f'./ReadyToSend/{stripped_guest_name}.txt', mode='w') as guest_files:
            guest_files.write(replaced_list)
