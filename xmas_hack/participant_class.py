import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.assigned_recipient = None
        
    def assign(self, lst):
        remaining_participants = [p for p in lst if p != self]
        self.assigned_recipient = random.choice(remaining_participants)
        self.assigned_recipient.assigned_recipient = self

    def __str__(self):
        if self.assigned_recipient:
            return f"🎅 {self.name} is Secret Santa for {self.assigned_recipient.name} "  # Fix: Change from 'self.secret_santa.name' to 'self.assigned_recipient.name'
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

    for participant in participants:
        participant.assign(participants)

    shuffle(participants)
    for participant in participants:
        print(participant)

if __name__ == "__main__":
    main()
