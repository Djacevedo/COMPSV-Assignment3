# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,name):
        new_node=Node(name)
        if not self.front:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_name=self.front.data
        self.front=self.front.next
        if not self.front:
            self.rear=None
        return removed_name
    
    def peek(self):
        if not self.front:
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def print_queue(self):
        if not self.front:
            print("(empty)")
            return
        current=self.front
        while current:
            print(f"={current.data}")
            current=current.next


def run_help_desk():
    # Create an instance of the Queue class
    queue=Queue
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            name=input("Enter cutomer name: ")
            queue.enqueue(name)
            print(f"{name} had been added to the queue.")
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped=queue.dequeue()
            if helped:
                print(f"Helped- {helped}")
            else: 
                print("No customer helped.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            next_customer=queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers next.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
