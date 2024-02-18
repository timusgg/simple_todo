from prettytable import PrettyTable

class to_do_list:
    def __init__(self):
        self.todo_list = []
        print('To-Do List created successully.')
    
    def __str__(self):
        table = PrettyTable()
        table.field_names = ["Task No.", "Task Name", "Status"]
        table.align = 'l'

        for num, task in enumerate(self.todo_list):
            name, status = task
            if status:
                status = "Complete"
            else:
                status = "Incomplete"
            table.add_row([num+1, name, status])
        
        return str(table)

    def add_task(self):
        print('== Add a task to the list == \n')
        title = input("Enter the title of the task : ")
        if input == '':
            print('Please enter a title !!!!!')
        else:    
            self.todo_list.append([title, False])
            print('Task added successfully!')

    def remove_task(self):
        print('== Remove a task from the list ==')
        print(self)
        print('Please enter the task number, the list is presented above.')
        task_number = input('Task Number to be removed :') 
        try:
            name = self.todo_list[task_number][0]
            self.todo_list.pop(task_number)
            print(f'Task {name} removed from the list successfully!')
        except TypeError or IndexError:
            print('Please enter a valid task number!!!')

    def change_status(self):
        print('== Change status of a task. ==')
        print(self)
        print('Please enter the task number, the list is presented above.')
        task_number = input('Task Number for status change : ')
        try:
            name, status = self.todo_list[task_number]
            if not status: 
                self.todo_list[task_number][1] = True
                print(f'Status of task {name} changed successfully !')
            else:
                self.todo_list[task_number][1] = False
                print(f'Status of task {name} changed successfully !')
        except TypeError or IndexError:
            print('Please enter a valid task number!!!')
        
    def show_list(self):
        print(self)

    def save_list(self):
        with open('todo_list.txt', 'w') as output_file:
            print(self, file=output_file)
        print('The list is saved to todo_list.txt file in the same directory.')

    def quit(self):
        print('Exiting.')
        exit()



options = {'1': 'Add Task', 
           '2': 'Remove Task', 
           '3': 'Change Status',
           '4': 'Show List', 
           '5': 'Save List',
           '6': 'Quit'}



def menu():
    table = PrettyTable()
    table.field_names = ["Option", "Description"]
    table.align = 'l'
    for num, option in options.items():
        table.add_row([f"({num})", option])

    print(table)



#driver code

def main():
    print('This is a simple to-do list program.\n')
    created_list = to_do_list()
    input('Press any key to continue...')   
    while True:
        menu()
        selection = input('Please select an (option). : ')

        if selection not in str(options) or selection == '':
            print('Please enter a valid option.')
        else:
            selected = options[selection].lower().replace(' ', '_')
            getattr(created_list, selected)()

        
if __name__ == '__main__':
    main()