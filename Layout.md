
Algorithmic Approach: Secret Santa

1. Problem Statement: List of Secret santa, who each person has, and list to be kept secret until a certain date

2. Algorithm:
   - Interactive experience: allow user to input names, this can be the first thing we do
	- We can either allow user to first input number of participants
	- Or we can try and implement a way for user to input people until a certain date, then once the date hits, then they cant add anymore, and the list is finalized
	- If we go ^this route, we can allow the user to enter how many days until finalized list i.e. 2 weeks from event date (dont want this to be christmas cause its pretty arbitary, cause people hold secret santa random days)
   - Maintain a list of participants & those who need still need to be assigned a person
	- We can use random function to create a new list of participants
	- If the random person == name of person we are trying to assign
	- While were assigning, once assignment is done, we can take out that person from one of the lists, so we can have a list of people who still need assignment
   - We need to implement one of the sort methods
	- I just dont know what part of this we would need to use this, cause we already use randomize feature to create a list, maybe we can just sort finalized list based on letter?
   - Design a simple front-end using HTML and CSS to collect participant names and display the final Secret Santa assignments
	- This is making it seem like we need a DB
   - Participants should keep their assigned recipient confidential until the gift exchange.
	- We can do something where a participant can enter their name, and the site will output who they were assigned to (this is a reach, but one way to implement this)
   - As each person/vendor is written down on the guest list, the original shopping list will update with what is left to buy/bring
   - At then end, there will be a final list of guests, items, and what is left to buy.

3. Pseudocode:

```plaintext
Algorithm Secret Santa:

Backend: 
    Initialize a list called guests
    Initialize a list called foodlist: user will put in a list of everything that is needed
    Initialize a list called drinkslist: user will put in a list of everything that is needed
    Initialize an empty list called food_confirmed: this will eventually tell the user what else is needed for the event
    Initialize an empty list called drinks_confirmed: left: this will eventually tell the user what else is needed for the event
    Initialize an empty list called overflow 

    Ask the user for the capacity
        - If the guest list is longer than the capacity, return an error message
    If there is a guest/vendor list submitted already, it will be split into a list using commas as a delimiter

    Loop: (optional, if the initial list was not already inputted by the user)
        Entering the guest/vendor to add ot the guests list
        The loop will end once the list becomes the same size as the capcity, or when the user wants to stop adding guests

    Loop: will keep track of what everyone is bringing
        The loop will be based on the length of the 2 foodconfirmed and drinksconfirmed lists
        The loop will go on until the length of the 2 lists is equal to the guest list size, or when the user says to stop
        The loop will ask if the person/vendor is bringing food or drinks
            If the answer is food:
                Will ask for user for what they will bring and will append to the food_confirmed list
            If the answer is drinks:
                Will ask for user for what they will bring and will append to the drinks_confirmed list                
            If the answer is neither, then it will ask and guide the user on how to answer the question
                Print an error message
    
    Loop: This will compare both confirmed food/drink lists with the foodlist and drinkslist
        For each item in the confirmed food/drinks list, it will edit the foodlist and drinkslist by deleting each item one by one
        If there is an error based on an excess of an item, that item will be appended to the overflow list
        After this list is done, the foodlist and drinkslist will show what items need to be taken care of 
        As well as a list of all the items there is an excess of 
```

Flowchart:

```flowchart
start --> [User Wants to plan an event]
<What is the capacity?>
Try --> [What is the guest_list] --> split this input to a list
if (length of guest_list) --> |Greater than capacity| [Give an error message]
<What is the food_list? : everything you need for the event>
<What is the drinks_list? : everything you need for the event>
while (length of guest list) --> |Less than capacity| [Ask user for person/vendors name]
while (length of guest list) --> |User wants to stop adding to list| [Loop Stops]
while (length of confirmed food/drinks list) --> |Less than capacity| [User/vendor will input what they are bringing] 
if (What person/vendor is bringing) --> |Food| --> [food_confirmed will be appended with answer]
if (What person/vendor is bringing) --> |Drinks| --> [drinks_confirmed will be appended with answer]
if (What person/vendor is bringing) --> |Anything but food or drinks| --> [error message will show up]
while (length of foodconfirmed) + (length of drinksconfirmed) --> |greater than 0|
if (item is food) --> |is in foodlist| --> [Delete that item from the foodlist]
if (item is food) --> |is not in foodlist| --> [Add that item to the overflow list]
if (item is drinks) --> |is in drinkslist| --> [Delete that item from the drinkslist]
if (item is drinks) --> |is not in drinkslist| --> [Add that item to the overflow list]
print (overflow list)
print (drinkslist)
print (foodlist)
print (guest_list)
```

This algorithm outlines a simple solution for an event planner. It helps the planner keep track of the food and drink items they need, as well as the guests. The planner will be able to input the venue size, as well as a list of the food and drinks they will need for the event. If the planner is hosting a pot-luck type of event, they will be able to keep track of who is bringing what. If this is an event with vendors, this algorith can handle that as well. At the end of the process, the planner will have a list of all the guests/vendors, as well as what items there is a surplus/shortage of. 

Please note that real-world applications of such systems can be more complex and may require additional features, user authentication, error handling, and scalability considerations. The provided solution serves as a basic example for educational purposes.

'''
PAUL'S INITIAL ATTEMPT, TRYING TO DO EXTRA CREDIT IN TIME
capacity = int(input('What is the capacity? ')) #need to make sure the venue can hold all persons
guests =  input('What is your guest list? Please separate each item with a comma') #need to to separate the list out to see all attendees
guest_list = guests.split(',')

if len(guest_list) > capacity:
    print("You're too popular, you need less friends")

food_list = input('What is your food list? Please separate each item with a comma') #need to to separate the list out later
drinks_list = input('What is your drinks list? Please separate each item with a comma') #need to to separate the list out later

food_list = food_list.split(',') #taking away from this  dictionary later 
drinks_list = drinks_list.split(',') #taking away from this dictionary later 

while len(guest_list) < capacity: #once the guest list exceeds capacity, stop adding
    answer = input("What is the person's name?, type 'done' if you are done ") #if there are less people than the capacity, edgecase 
    if answer == 'done':
        break
    guest_list.append(answer) #adding to guest list

print(guest_list) 
food_drink = {'food':food_list , 'drinks':drinks_list} #create a dictionary to see what is being brought 

while len(food_drink['food']) + len(food_drink['drinks'])< (len(guest_list)): #limits the question to the amount of people coming, and handles invalid inputs
    x = input('Will you be bringing food or drinks?')
    if x.lower() == 'food':
       item = input('What item is it?')
       food_drink['food'].append(item) #if food, add to the 'food' list in the dictionary 
    elif x.lower() == 'drinks':
        item = input('What item is it?')
        food_drink['drinks'].append(item) #if drinks, add to the 'drinks' list in the dictionary 
    elif x.lower() != 'food' or 'drinks':
        print('Invalid input, please type "food" or "drinks"') #handles invalid input
       
       
print(food_drink) # make a way to see if all the items in the list have been met, and print that each time the question is asked
'''