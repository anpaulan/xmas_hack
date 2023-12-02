import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
    
    '''
    def adding inputs to instantiate:
        part_list = []
        for i in site_list(): 
            part_list.append(i)
    '''        
    
    
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
    
''' #this is me trying to make a dict so that people can be reminded of who their assignment is, doesnt work right now, and might not be worth putting time into this.
    for part, assignments in final_list.items():
        print(f'{part} - {assignments}')
    
    print(f'{final_list.items}')
'''        

def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]


if __name__ == "__main__":
    main()
