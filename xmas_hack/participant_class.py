import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
    
    def assign(self, lst):
        potential_recipients = [p for p in lst if p != self and p.assigned_recipient is None]

        for participant in lst:
            if participant != self and self.assigned_recipient is None:
                valid_recipients = [p for p in potential_recipients if p != self.assigned_recipient]

                if valid_recipients:
                    recipient = random.choice(valid_recipients)
                    self.assigned_recipient = recipient
                    recipient.assigned_recipient = self
                    potential_recipients.remove(recipient)
                    break

    def __str__(self):
        if self.assigned_recipient:
            return f"🎅 {self.name} is the Secret Santa for {self.assigned_recipient.name}"
        else:
            return f"🎅 {self.name} doesn't have a Secret Santa"

        
def shuffle(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]           
    
def main():
    participants = [
        Participant("Paul"),
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
