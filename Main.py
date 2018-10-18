#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: Main.py
Name: Angel Villalpando
Date: 10/17/2018
Course: CS 2302 - Data Structures

"""

class Node(object):  # basic Node class, as per lab-description
    def __init__(self, password):
        self.password = password
        self.count = 1
        self.next = None

class LinkedList(object):  # linked list class
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, data): # this method inserts into the linked list, but only updates the 'count' if duplicate
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.size += 1
            return

        curr = self.head

        while curr is not None:  # checks duplicate, only updates the count
            if curr.password == newNode.password:
                curr.count += 1
                break

            elif curr.next is None:
                curr.next = newNode
                self.size += 1
                break

            curr = curr.next

    def print_list(self):  # this is the Linked List print method
        printval = self.head
        while printval is not None:
            print(printval.password, printval.count)
            printval = printval.next

    def print_top_20(self):  # This is also a linked list method, but only for the top 20 passwords used
        curr = self.head
        print("The top 20 passwords are: ")
        print("-------------------------")
        for i in range(20):
            print("Password: ", curr.password)
            print("Count: ", curr.count, "\n")
            curr = curr.next

    def bubble_sort(self): # this is a bubble sort method. The information in the Nodes is swapped, not the Nodes
        if self.size > 1:
            for i in range(self.size-1):
                current = self.head
                for j in range(self.size-1-i):
                    if current.count < current.next.count:
                        tempCount = current.count
                        tempPassword = current.password
                        current.count = current.next.count
                        current.password = current.next.password
                        current.next.count = tempCount
                        current.next.password = tempPassword
                    current = current.next


def merge_sort(list): # merge sort method for list sorting

    curr1 = list  # temporary iterator to obtain the midpoint of the list
    mid = size_update(list) / 2  # determines mid point for iteration

    if list == None or list.next == None:
        return list

    while mid-1 > 0:
        curr1 = curr1.next  # gets to mid point
        mid = mid - 1

    curr2 = curr1.next
    curr1.next = None
    curr1 = list

    left = merge_sort(curr1)  # creates left half of list
    right = merge_sort(curr2) # creates right half of list

    return merge(left, right) # merges already sorted halves


def merge(left, right):
    if left == None and right == None:
        return None
    if left == None:
        return right
    if right == None:
        return left

    if left.count < right.count:  # merges the parameter "halves" in descending order
        final = right
        final.next = merge(left, right.next)
    else:
        final = left
        final.next = merge(left.next, right)

    return final


def size_update(list): # size updater is called on every recursive of merge sort and is updated
    size = 0
    curr = list
    while curr is not None:
        size = size + 1
        curr = curr.next

    return size

def print_node_dictionary(dict, node):  # This prints the dictionary when each index is a linked list "head"
    curr = node.head
    while curr != None:
        print("Password: ", dict[curr.password].password)
        print("Count: ", dict[curr.password].count, "\n")
        curr = curr.next

def print_20_dict(dictionary, node):  # This prints the top 20 from linked list dictionary
    curr = node.head
    for k in range(20):
        print("Password: ", dictionary[curr.password].password)
        print("Count: ", dictionary[curr.password].count, "\n")
        curr = curr.next

def dictionary_populator(dictionary, node): # this method populates the linked list dictionary, during file read
    current = node.head
    while current != None:
        dictionary[current.password] = current
        current = current.next

def non_sort_dictionary_populator(dictionary, item): # This method populates the dictionary straight from the file
        if item in dictionary:  # checks for duplicates
            dictionary[item] = dictionary[item] + 1
        else:
            dictionary[item] = 1

def print_dictionary(dict): # This prints the dictionary contents when the values at index are NOT Linked Lists
    for item in dict:
        print("Password: ", item)
        print("Count: ", dict[item], "\n")

def main():

    file = open("passwordTester2.txt", "r", encoding="ISO-8859-1") # encoding used to correct error at file read

    bubblePasswordList = LinkedList() # list to be sorted by Bubble Sort
    mergePasswordList = LinkedList() # list to be sorted by the Merge sort
    nonSortDict = {} # dictionary with NO LINKED LIST indices
    sortedDict = {} # Linked List dictionary

    for line in file:    ## This populates all of the lists and dictionaries as the file is being read
        justPassword = line.strip('\n').partition('\t')
        bubblePasswordList.insert(justPassword[2])
        mergePasswordList.insert(justPassword[2])
        non_sort_dictionary_populator(nonSortDict, justPassword[2])

    file.close()

    print("\n***** Using Bubble Sort *******")
    bubblePasswordList.bubble_sort()
    bubblePasswordList.print_top_20()

    print("****** Using Merge Sort *******")
    merge_sort(mergePasswordList.head)
    mergePasswordList.print_top_20()

    print("\nPre-Sorted Dictionary: ")
    print("----------------------")
    print_dictionary(nonSortDict)

    print("\nPost-Sorted Dictionary")
    print("----------------------")
    dictionary_populator(sortedDict, bubblePasswordList)
    print_node_dictionary(sortedDict, bubblePasswordList)



main()
