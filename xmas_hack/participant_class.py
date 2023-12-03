import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
    
    def assign(self, participants_list):
        choices = list(participants_list)
        index = choices.index(self)
        max_index = len(choices) - 1
        
        for i in range(len(choices)):
            if index == max_index:
                self.assigned_recipient = choices[0]
            else:
                self.assigned_recipient = choices[index + 1]

            index += 1
            if index > max_index:
                index = 0

            choices = choices[1:] + [choices[0]]  
            if self.assigned_recipient != self and self.assigned_recipient.assigned_recipient != self:
                break
       
    def __str__(self):
        if self.assigned_recipient:
            return f"🎅 {self.name} is the Secret Santa for {self.assigned_recipient.name}"
        else:
            return f"🎅 {self.name} doesn't have a Secret Santa"

    '''
            secret_person = random.choice(choices)
            while secret_person == person and secret_person.assigned_recipient == person:
                secret_person = random.choice(choices)
            person.assigned_recipient = secret_person
            choices.remove(secret_person)
    '''
        
def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]           
    
def main():
    participants = [
        Participant("Peter"),
        Participant("Efraim"),
        Participant("Jessica"),
        Participant("Asha"),
        Participant("Santa")
    ]

    shuffle(participants)
    for participant in participants:
        participant.assign(participants)
        print(participant)

if __name__ == "__main__":
    main()
