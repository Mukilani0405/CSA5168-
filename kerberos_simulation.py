import random

# Authentication Server
ticket = random.randint(1000, 9999)

print("AS Generated Ticket:", ticket)

# Client receives ticket
client_ticket = ticket

# Service Server Validation
server_ticket = ticket

if client_ticket == server_ticket:
    print("Authentication Successful")
else:
    print("Authentication Failed")
