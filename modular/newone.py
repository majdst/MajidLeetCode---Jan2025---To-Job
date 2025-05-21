import math
import rectangular
import circular

#constant for the menu choices

area_cicle_choice = 1
circumference_choice = 2
area_rectangular_choice = 3
perimeter_rectangular_choice = 4
quit_choice = 5

def display_menu():
    print('MENU')
    print('1) Area of Circle')
    print('2) Circumference of a Circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangular')
    print('5) Quit')

def main():
    
    #control the variable
    choice = 0
    
    while choice != quit_choice:
        
        #Display the menu
        display_menu()
        choice = int(input('Please Enter your choice: '))
        
        if choice == area_cicle_choice:
            
            #Ask user
            radius = int(input('Please Enter a value of radius: '))
            
            print(f'The area of circle is: {circular.area(radius)}')
        elif choice == circumference_choice:
            
            #Ask User
            radius = int(input('Please enter a value of radius: '))
            print(f'The circumference of circle is: {circular.circumference(radius)}')
            
        elif choice == area_rectangular_choice:
            
            length = int(input('Please enter a value: '))
            width = int(input('Please enter a value: '))
            
            print(f'The Area of rectangular is: {rectangular.area(width, length)}')
        
        elif choice == perimeter_rectangular_choice:
            length = int(input('Please enter a value: '))
            width = int(input('Please enter a value: '))
            
            print(f'The Area of rectangular is: {rectangular.perimeter(width, length)}')
        else:
            print('Quit')
            
main()
        