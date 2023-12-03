
import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
   
    
    def assign(self, lst):
            
    # remaining_participants = [p for p in lst if p != self] # part of Ulises initial code, current is fixed version
        remaining_participants = [p for p in lst if p != self]
        self.assigned_recipient = random.choice(remaining_participants)
        self.assigned_recipient.assigned_recipient = self
        # remaining_participants = [p for p in lst if p != self] # part of Ulises initial code, current is fixed version
        # remaining_list = lst[:]
        # pairs = dict()
        # while len(remaining_list) < 0:
        #     for person in lst:
                
        #         for giver, recipient in pairs.items():
        #             giver.assigned_recipient = recipient
        #         return pairs
            
    '''
        for person in lst: # assigning each person to no one for now
            if person != self and person.assigned_recipient is None and person.assigned_recipient not in remaining_list:
                self.assigned_recipient = person
                person.assigned_recipient = self
                remaining_list.remove(self)
                    '''          
    def __str__(self):
        if self.assigned_recipient:
            return f"🎅 {self.name} is the Secret Santa for {self.assigned_recipient.name} "  # Fix: Change from 'self.secret_santa.name' to 'self.assigned_recipient.name'
        else:
            return f"🎅 {self.name} doesn't have a Secret Santa"
        
def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]           
'''
            asspaired[person] = None

        for participant in lst:
            buying_for = False
            for i in paired:
                if paired[i] is None and i != participant and i not in paired.values():
                    participant.assigned_recipient = i
                    paired[participant] = i.name
                    paired[i] = participant.name
                    buying_for = True
            if buying_for:
                break
        return paired
'''            
        
            # if participant != self:
            #     if remaining_participants:
            #         participant.assigned_recipient = remaining_participants.pop()
    
    # def forgot(self,name) :
    #     user = input("What is your name?")
    #     if user == self.name:
    #         return self.assigned_recipient.name

    
def main():
    partihjkhcipants = [
        Participant("Paul"),
        Participant("Peter"),

    ]
    participants = []
    user_input = input("Enter participant names separated by commas: ")

    new_participant_names = [name.strip() for name in user_input.split(',')]
    for name in new_participant_names:
        new_participant = Participant(name)
        participants.append(new_participant)
        print(f"Added participant: {new_participant.name}")

    one_participants = participants.copy()
    print(type(participants))
    for x in range(0, len(one_participants) -1):
                one_participants[x].assign(one_participants[x+1])
                if x == len(one_participants) -1:
                    one_participants[len(one_participants) -1].assign(one_participants[0])

    print("\nSecret Santa Assignments:")
    for participant in participants:
        print(f"{participant}")
        # final_list[participant] = participant.assign(participants) #Dictionary is not working as intended
    
''' #this is me trying to make a dict so that people can be reminded of who their assignment is, doesnt work right now, and might not be worth putting time into this.
    for part, assignments in final_list.items():
        print(f'{part} - {assignments}')
    
    print(f'{final_list.items}')
'''        

# def shuffle(lst):
#     for i in range(len(lst) - 1, 0, -1):
#         j = random.randint(0, i)
#         lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()


''' original
class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
    

    def adding inputs to instantiate:
        part_list = []
        for i in site_list(): 
            part_list.append(i)

    
    
    def assign(self, lst): 
        # remaining_participants = [p for p in lst if p != self] # part of Ulises initial code, current is fixed version
        remaining_participants = lst[:]
        for participant in lst:
            if participant != self:
                if remaining_participants:
                    participant.assigned_recipient = remaining_participants.pop()
                
    def forgot(self,name) :
        user = input("What is your name?")
        if user == self.name:
            return self.assigned_recipient.name
        
    def __str__(self):
        if self.assigned_recipient:
            return f"🎅 {self.name} is the Secret Santa for {self.assigned_recipient.name} "  # Fix: Change from 'self.secret_santa.name' to 'self.assigned_recipient.name'
        else:
            return f"🎅 {self.name} doesn't have a Secret Santa"

    
def main():
    participants = [
        Participant("Paul"),
        Participant("Peter"),
        Participant("Efraim"),
        Participant("Jessica"),
        Participant("Asha"),
        Participant("Santa")
    ]
    
    forgetful = participants.forgot('Paul') #not working
    
    # final_list = dict()
    shuffle(participants)
    for participant in participants:
        # final_list[participant] = participant.assign(participants) #Dictionary is not working as intended
        print(participant)
    
#this is me trying to make a dict so that people can be reminded of who their assignment is, doesnt work right now, and might not be worth putting time into this.
    for part, assignments in final_list.items():
        print(f'{part} - {assignments}')
    
    print(f'{final_list.items}')


def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()
    
'''
