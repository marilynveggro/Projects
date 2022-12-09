class MenuList():
    # Generates a new  user password
    def PasswordGenerator(self):
        generatedPassword = ''
        passwordLength = random.randint(6, 8 )
        for character in range(0, passwordLength):
            generatedPassword = generatedPassword + LETTERS[random.randint(0, len(LETTERS) - 1)]
        return generatedPassword

    @staticmethod
    def Main_Menu():
        # Menu option
        print("\nSelect from the following choices: ")

        print("\n0: Exit ")
        print("1: Submit helpdesk ticket ")
        print("2: Show all tickets ")
        print("3: Respond to ticket by number ")
        print("4: Re-open resolved ticket ")
        print("5: Display ticket stats ")
        print("-------------------------------------------------------------------")

        enter_menu_selection = int(input("Enter Menu Selection 0 - 5: "))
        print("-------------------------------------------------------------------")
        return enter_menu_selection


def Process_Input(selection, menu):
    if selection == 0:
        print("Thank you, see you later.");
        exit(0);
    if selection == 1:
        Submit_helpdesk_ticket(menu);
    if selection == 2:
        show_tickets()
    if selection == 3:
        answer_ticket_by_id()
    if selection == 4:
        open_ticket_by_id()
    if selection == 5:
        display_ticket_stats()


def Submit_helpdesk_ticket(menu): #Information request
    Id = str(input("Enter your Staff Id: "))
    Name = str(input("Enter your Name: "))
    Email = str(input("Enter your Email: "))
    print("If you require a new password type: Password Change");
    user = User(Id, Name, Email, "");
    problem = str(input("\nEnter description of problem: "))
    ticket = Ticket(user, problem)

    if problem == "Password Change": #Generate a new  user password
        password = menu.PasswordGenerator();
        print("This is your new password: " + password)
        ticket.closeTicket("User password was set to: " + password)

    USERS.append(user)
    TICKETS.append(ticket)
    print("\nTicket has been submitted to the helpdesk queue")

    extra_problem = str(input("\nDo you have another problem to submit? (Y/N)"))
    print("-----------------------------------------------------------------------")
    if extra_problem == "Y":
        Submit_helpdesk_ticket(menu)

import random

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
TICKETS = []
USERS = []


class User(object):
    def __init__(self, Id, Name, Email, Password):
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Password = Password


class Ticket(object):
    # Generate open and close tickets
    ticket_id = 1

    def __init__(self, user, problem, status="open"):
        self.user = user
        self.problem = problem
        self.status = status
        self.id = int(Ticket.ticket_id)
        self.response = ""
        Ticket.ticket_id = Ticket.ticket_id + 1

    def openTicket(self, updatedProblem):
        self.problem = updatedProblem
        self.status = "open"

    def closeTicket(self, response):
        self.response = response
        self.status = "closed"


def show_tickets():
    for ticket in TICKETS: #Generate ticket resume
        print("Ticket: " + str(ticket.id))
        print("Submitted by Staff Id: " + str(ticket.user.Id))
        print("Ticket Owner: " + ticket.user.Name)
        print("Contact Email: " + ticket.user.Email)
        print("Description Of Issue: " + ticket.problem)
        print("Status: " + ticket.status)
        print("Response: " + ticket.response)
        print("-------------------------------------------------------------------")

def answer_ticket_by_id(): #answer ticket
    ticket_number = int(input("Which ticket would you like to answer?"))
    ticket = findTicketId(ticket_number)
    print("Description of the problem: " + ticket.problem)
    ticket_response = str(input("Please enter your response: "))
    ticket.closeTicket(ticket_response)
    print("-----------------------------------------------------------------------")

def open_ticket_by_id():
    ticket_number = int(input("Which ticket would you like to open?"))
    ticket = findTicketId(ticket_number)
    ticket.openTicket(str(input("Write the updated problem?")))
    print("-----------------------------------------------------------------------")

def display_ticket_stats():
    open = 0
    resolved = 0
    totalTickets = 0


    for ticket in TICKETS:
        totalTickets = totalTickets + 1
        if ticket.status == "closed":
            resolved = resolved + 1
        elif ticket.status == "open":
            open = open + 1

    print("Submitted Tickets:" + str(totalTickets))
    print("Open Tickets:" + str(open))
    print("Resolved Tickets:" + str(resolved))


def findTicketId(id):
    for ticket in TICKETS:
        if ticket.id == id:
            return ticket


def Main():
    menu = MenuList();
    selected_option = menu.Main_Menu()
    Process_Input(selected_option, menu)
    Main()



# start
Main()
