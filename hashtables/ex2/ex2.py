#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    #go through the tickets and insert the source and destinations into the ht
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        current_location = "NONE"

    # loop through to prepare to make the path
    for i in range(length):
    # once it finds the source(0), start by retrieving the none in source and start the route
        route[i] = hash_table_retrieve(hashtable, current_location)
        current_location = route[i]


    # pop the last item in the array to get rid of "NONE"
    route.pop()
    #return route
    return route
