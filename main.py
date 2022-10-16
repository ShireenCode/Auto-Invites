with open("./Input/Names/invited_names.txt", "r") as invitees:
    invitee_list = invitees.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    template = starting_letter.read()
    print(template)

for invitee in invitee_list:
    new_invitee = invitee.strip()
    new_invitee = new_invitee.strip("/n")
    with open(f"./Output/ReadyToSend/{new_invitee}.txt", "w") as letter:
        letter.write(str(template).replace("[name]", str(new_invitee)))
