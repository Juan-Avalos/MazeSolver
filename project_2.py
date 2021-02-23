#Juan Avalos
#11/17/2019
#Assignment #4
#CS - 1411
#Create a program to solve the given maze

#1. Open file that has a maze
#2. Brake down the maze into individual strings and list
#3. Create handles that handles all the errors if error is found like no
# start, no end, maze unsolveable, no file, file empty, and if file contains invalid characters
#4. Create a function that repeats to build the maze
#5. Find the starting point
#6. Create a function that can solve the maze and has back tracking    
#7. Find the end and stop

#need to implement maze unsolveable, file is empty, and invalid character errors

#function defines every other function



def main():
#works
    filename = input("Enter a file name:" )
    #tries the things inside
    
    try:
    #opens the file
        open_maze = open(filename, 'r')
        #empty list
        Mlist = []
        #every line in file
        for lines in open_maze:
            #strips lines and turns into a list
            Clist = list(lines.strip('\n'))
            #append every character of Clist into list
            Mlist.append(Clist)
        #print(Mlist)

        #if the list has nothing appended tp it and equals 0 then no maze    
        if len(Mlist) == 0:
            return (print("Error: Specified file contains no maze."))
        
        #change name of maze
        broken_maze = Mlist
        #print(broken_maze)
        #maze(broken_maze)
        
    #letter = the function that finds 'S', this function also tranfers the broken_maze
        letter = finding_S(broken_maze)
        
    #finds 'E' and makes sure its in the maze
        finding_E(broken_maze)
        if finding_E(broken_maze) == False:
            return (print("Error:No end position found\n"))
        
    #finds 'S' and makes sure its in the maze    
        searching_S(broken_maze)
        if searching_S(broken_maze) == False:
            return (print("Error:No start position found\n"))
        
    #finds if there is a invalid character and its location
        position, symbol = invalid_char(broken_maze)
        if (position > 0):
            return (print("Error:Maze contains unvalid characters. Line", position,"contains invalid character","'"+symbol+"'"))

    #prints maze
        maze(broken_maze)    
    #Once letter is found it comes back as two integers, the first one is rows and the second is spaces    
        rows = letter[0]
        ##print(rows)
    #spaces is the each character value 
        spaces = letter[1]
        ##print(spaces)
        
    #The last function of the program which does the solving of the maze, also call rows, spaces, and the broken_maze
        solve(rows, spaces, broken_maze)
    #close file
        open_maze.close()
    #if no file 
    except FileNotFoundError:
         print("Error:Specified file does not exist")
         

  
#finding starting point    
def finding_S(maze):
#every list within the larger list of the maze
    for rows in maze:
#every character within the list of the larger list
        for spaces in rows:
#if 'S' is in spaces
            if 'S' in spaces:         
#letter = the exact list within the large list that the 'S' is in, and where within the list is the character at
                letter = (maze.index(rows), rows.index(spaces))
                #print(letter)
                #returns the found letter back to the main function
                return letter

#finding E    
def finding_E(maze):
    #defining E
    E_value = 'E'
    found_E = False
#every row of list within the full maze
    for rows in maze:        
#every individual character in each row
        for spaces in rows:
#if one of the characters is the E value
           if E_value in spaces:
               return True               
    return False

#finding S
def searching_S(maze):
    #defining S
    S_value = 'S'
    found_S = False
#every row of list within the full maze
    for rows in maze:
#every individual character in each row
        for spaces in rows:
#if one of the characters is the S value
            if S_value in spaces:
                return True
    return False

#checks if a character is in the maze and invalid
def invalid_char(maze):
    #define valid characters to ignore
    valid = ['S', 'E', ' ', '#']
    #set a value to zero which either adds or doesnt, if character is true
    spot = 0
    #every row of list in the maze
    for rows in maze:
    #every character in each row of list  
        for spaces in rows:
            #print(spaces)
            #decides if a character that is not valid is in maze and if it is add the amount of rows
            if spaces not in valid:
                #print(rows)
                #return number of rows and the invalid character
                return spot, spaces
        #adds if invalid charcter is True
        spot += 1
    #if no invalid character return 0, nothing happens
    spot = 0
    return spot, '1'

#function prints the maze all in one print
def maze(broken_maze): 
#blank string
    maze_figure = ''
    #every row of list in maze
    for rows in broken_maze:
        #join all rows of the maze into string
        bro_maze = ''.join(rows)
        #add every row and delete extra space 
        maze_figure += bro_maze + '\n'
    #prints maze
    print(maze_figure)
    print() 
       
#this function solves the maze           
def solve(rows, spaces, given_maze):
#make a loop to repeat the solving
    loop = 2
#two empty list to append and defien the boundaries
    amount_rows = []
    amount_spaces = []
    #lenth of the rows
    for i in range(len(given_maze)):
        amount_rows.append(i)
        #print(amount_rows)
    #lenth of the rows
    for i in range(len(given_maze[0])):
        amount_spaces.append(i)
        #print(amount_spaces)
        
#while loop = 2, find path
    while(loop == 2):
#from starting position S if white space is either left, right, up,, or down move the starting position that way to not delete S
        #if left white is Trrue
        if given_maze[rows][spaces] == 'S' and given_maze[rows][spaces - 1] == ' ':
            spaces -= 1
        #if right white space is True
        if given_maze[rows][spaces] == 'S' and given_maze[rows][spaces + 1] == ' ':
            spaces += 1
        #if up white space is true
        if given_maze[rows][spaces] == 'S' and given_maze[rows - 1][spaces] == ' ':
            rows -= 1
        #if down white space is True
        if given_maze[rows][spaces] == 'S' and given_maze[rows + 1][spaces] == ' ':
            rows += 1
#after every if statment if True it will print new maze            
#starting at the new starting point if below is white space and within the boudaries print the following symbol            
        if rows + 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows + 1][spaces] == ' ':
                given_maze[rows][spaces] = 'v'
                #add 1 to the rows which sets the starting point to the right
                rows += 1
                maze(given_maze)
                continue
#starting at the new starting point if the up is white space and within the boudaries print the following symbol           
        if rows - 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows - 1][spaces] == ' ':
                given_maze[rows][spaces] = '^'
                #subtracts 1 to the rows which sets the starting point up
                rows -= 1
                maze(given_maze)
                continue
#starting at the new starting point if the left is white space and within the boudaries print the following symbol
        if spaces - 1 in amount_spaces and rows in amount_rows:
            if given_maze[rows][spaces - 1] == ' ':
                given_maze[rows][spaces] = '<'
                #subtracts 1 to the spaces which sets the starting point to the left 
                spaces -= 1
                maze(given_maze)
                continue            
#starting at the new starting point if the right is white space and within the boudaries print the following symbol            
        if spaces + 1 in amount_spaces and rows in amount_rows:
            if given_maze[rows][spaces + 1] == ' ':
                given_maze[rows][spaces] = '>'
                #adds 1 to the spaces which sets the starting point to the right
                spaces += 1
                maze(given_maze)
                continue
#if next white space is 'E' loop becomes 1, which exits the loop
#starting at the new starting point if the right spaces is 'E' and with in the boudaries print the following symbol            
        if rows in amount_rows and spaces + 1 in amount_spaces:
            if given_maze[rows][spaces + 1] == 'E':
                #if the line above is true, the loop number changes to exit the loop
                loop = 1
                given_maze[rows][spaces] = '>'
                maze(given_maze)
                continue
#starting at the new starting point if the left spaces is 'E' and with in the boudaries print the following symbol            
        if rows in amount_rows and spaces - 1 in amount_spaces:
            if given_maze[rows][spaces - 1] == 'E':
                #if the line above is true, the loop number changes to exit the loop
                loop = 1
                given_maze[rows][spaces] = '<'
                maze(given_maze)
                continue
#starting at the new starting point if the down spaces is 'E' and within the boudaries print the following symbol            
        if rows + 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows + 1][spaces] == 'E':
                #if the line above is true, the loop number changes to exit the loop
                loop = 1
                given_maze[rows][spaces] = 'v'
                maze(given_maze)
                continue
#starting at the new starting point if the up spaces is 'E' and within the boudaries print the following symbol            
        if rows - 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows - 1][spaces] == 'E':
                #if the line above is true, the loop number changes to exit the loop
                loop = 1
                given_maze[rows][spaces] = '^'
                maze(given_maze)
                continue
#back tracking           
#if stuck and spaces to the left is a symbol to the right and within the boudaries replace symbol         
        if rows in amount_rows and spaces - 1 in amount_spaces:
            if given_maze[rows][spaces - 1] == '>':
                given_maze[rows][spaces] = '.'
                #subtracts 1 to the spaces which sets the starting point to the left 
                spaces -= 1
                maze(given_maze)
                continue
#if stuck and spaces to the right is a symbol to the left and within the boudaries replace symbol           
        if spaces + 1 in amount_spaces and rows in amount_rows:
            if given_maze[rows][spaces + 1] == '<':
                given_maze[rows][spaces] = '.'
                #adds 1 to the spaces which sets the starting point to the right 
                spaces += 1
                maze(given_maze)
                continue
#if stuck and rows to below is a symbol to go up and within the boudaries replace symbol             
        if rows + 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows + 1][spaces] == '^':
                given_maze[rows][spaces] = '.'
                #adds 1 to the rows which sets the starting point to above 
                rows += 1
                maze(given_maze)
                continue
#if stuck and rows to above is a symbol to go down and within the boudaries replace symbol  
        if rows - 1 in amount_rows and spaces in amount_spaces:
            if given_maze[rows - 1][spaces] == 'v':
                given_maze[rows][spaces] = '.'
                #subtracts 1 to the rows which sets the starting point to below 
                rows -= 1
                maze(given_maze)
                continue
#maze unsolveable
    #if no more white spaces to move to route not possible
        if " " not in given_maze:
            return (print("Error: No route could be found from start to end. Maze unsolvable."))
#runs the entire program                            
main()
