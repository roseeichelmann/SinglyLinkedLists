#  File: TestLinkedList.py

#  Description: A program that creates functions for a linked list class

#  Student Name: Rose Eichelmann

#  Student UT EID: ree585

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7-30-21

#  Date Last Modified: 08-5-21

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):
        if self.first == None:
            return 0
        current = self.first
        num_links = 1
        # iterate until at last link and add to num links
        while current.next != None:
            current = current.next
            num_links += 1
        return num_links
        
    # add an item at the beginning of the list
    def insert_first (self, data): 
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last (self, data): 
        new_link = Link(data)
        current = self.first
        # if list is empty first link is new link
        if (current == None):
            self.first = new_link
            return
        # move through linked list until next link is none
        while (current.next != None):
            current = current.next
        # add new link to end
        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data): 
        new_link = Link(data)
        # move down list until next link is greater than new link
        current = self.first
        if current == None:
            self.first = new_link
            return
        after = current.next
        while current.next.data < new_link.data:
            current = current.next
            after = after.next
        current.next = new_link
        new_link.next = after

    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        current = self.first
        # return none if list is empty
        if (current == None):
            return None
        # move down list until link is found
        while (current.data != data):
            # if next is None then link is not in list
            if (current.next == None):
                return None
            else:
                current = current.next
        return current

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        current = self.first
        # return none if list is empty
        if current == None:
            return None
        while current.data != data:
            # return none if at end of list
            if current.next == None:
                return None
            # return none if past point that link could be
            elif current.data > data:
                return None
            else:
                current = current.next
        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        previous = self.first
        current = self.first
        # if list is empty return none
        if (current == None):
            return None
        # move through list until link is found
        while(current.data != data):
            # if next is None then link is not in list
            if (current.next == None):
                return None
            # move current to next link
            else:
                previous = current
                current = current.next
        # if link is first in list make self.first equal to the next link
        if (current == self.first):
            self.first = self.first.next
        # delete link
        else:
            previous.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first
        # print first link
        if current == None:
            return None
        num_links = 1
        while current != None:
            if num_links == 10:
                print(current.data)
                num_links = 1
            else:
                print(current.data, "  ", end="")
                num_links += 1
            current = current.next

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
        if self.first == None:
            return None
        new_list = LinkedList()
        current = self.first
        while current.next != None:
            new_list.insert_last(current.data)
            current = current.next
        new_list.insert_last(current.data)
        return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self): 
        if self.first == None:
            return None
        reversed = LinkedList()
        current = self.first
        while current != None:
            reversed.insert_first(current.data)
            current = current.next
        return reversed

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self): 
        return

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        if self.first == None:
            return True
        current = self.first
        while current.next != None:
            if current.next.data < current.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
        new_list = LinkedList()
        return

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        link1 = self.first
        link2 = other.first
        while link1 != None:
            if link1.data != link2.data:
                return False
            link1 = link1.next
            link2 = link2.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):
        new_list = LinkedList()
        current = self.first
        while current != None:
            if new_list.find_unordered(current.data) == None:
                new_list.insert_last(current.data)
            current = current.next
        return new_list

def main():

    # Test method insert_in_order()
    new_list2 = LinkedList()
    for i in range(12):
        new_list2.insert_last(i)
    new_list2.insert_last(20)
    new_list2.insert_in_order(15)
    new_list2.__str__()

    # # Test method get_num_links()
    # print(new_list2.get_num_links())

    # # Test method find_un    # new_list.__str__()ordered() 
    # # Consider two cases - data is there, data is not there 
    # print(new_list2.find_unordered(15))

    # # Test method find_ordered() 
    # # Consider two cases - data is there, data is not there 
    # print(new_list2.find_ordered(11))

    # # Test method delete_link()
    # # Consider two cases - data is there, data is not there 
    # print(new_list2.delete_link(50))
    # new_list2.delete_link(9)
    # print(new_list2.__str__())

    # Test method copy_list()
    new_list3 = new_list2.copy_list()
    new_list3.__str__()

    # Test method reverse_list()
    reversed = new_list2.reverse_list()
    reversed.__str__()

    # # Test method sort_list()


    # # Test method is_sorted()
    # # Consider two cases - list is sorted, list is not sorted
    # print(reversed.is_sorted())


    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()