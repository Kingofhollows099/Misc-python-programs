import random
import time

leavel = 'djbhsadbhfhsdfbhsadbhdhfgshdfhdhhddhhdhdhdhfashdfhesefuuhdfjasdfndsjfhjfjdhfufhdfjjhufndfjlsdfhlskdjfhdgjlkasfdfjhrutjkjyDLKJFJFGHDSJFJDFDFJLJDYTKDFJDSKFJDSKFJSDFKJFDJFFjjskfkekskdfjsekkdfkdkfw395678548605986349405685409rgkfdmgjkafgkaejfjk@#!$%**(&%&*&XHXGGXGXGXGXGxggcgdfjfkdkfkdjfehfdhf'

def helpp():
    print("Some commands you can do are:'timer', 'math', or 'games'(there will be more stuff added in the future).  ")
    print('You can also type "examples" to see python executables.')
    
while True:
    try:
        if leavel == 'leave':
            break
        print('Hello! To ask for help or if you dont know the commands,type "help" or "?"! You can also type "leave" to leave')
        print('the program!')
        
        while True:
            inputl = input()
    
            if inputl == "help":
                helpp()
        
            if inputl == '?':
                helpp()
            
            if inputl == 'Help':
                helpp()
            
            if inputl == 'math':
                print('You can choose "<# catchup to >#", "miles per hour", or "age calc"')
        
            if inputl == 'Math':
                print('You can choose "<# catchup to >#", "miles per hour", or "age calc"')
            
            if inputl == '<# catchup to >#':
                first = int(input('What is the first number? '))
                second = int(input('what is the second number? '))
                ahead = int(input('how far ahead is the first number? '))
                first1ajk = ahead
                second1ajk = 0
                counter = 0
                while first1ajk >= second1ajk:
                    first1ajk = first1ajk + first
                    second1ajk = second1ajk + second
                    counter = counter + 1
                print(counter)
                
            if inputl == 'miles per hour':
                n1 = int(input('What is the first number? '))
                n2 = int(input('What is the second number? '))
                n4 = int(input('How far does the second number need to go? '))
                n3 = n2 - n1 
                ans = n4 / n3
                print('the answer is' + ans)
            
            if inputl == 'age calc':
                year = input('What year were you born? ')
                bday = input('Has your birthday happend yet this year? (y/n) ')
                current_year = int(input('What year is it? '))
                year_int = int(year)
                age = current_year - year_int
                if bday == 'n':
                    age = age - 1
                print('Your current age is ' + str(age) + '!')
        
            if inputl == 'games':
                print('You can choose "guessing game" or " times up!"')
        
            if inputl == 'guessing game':
                while True:
                    a = 'Nope!'
                    b = 'Sorry!'
                    c = 'Sorry buddy, thats not it!'
                    d = 'I gotta say, no.'
                    e = 'No. thats the wrong number.'
                    f = 'Try again later.'
                    h = 'Oh well'
                    i = 'To bad'
                    j = 'Dont feel bad!'
                    k = 'To bad, so sad'
                    l = 'You dont have a clue do you?'
                    m = 'You suck at this!'
                    n = '*sigh*'
                    o = 'Could you at least try to do better?'
                    g = [a, b, c, d, e, f, h, i, j, k, l, m, n, o]
                    options = range(1, 51)
                    number = random.choice(options)
                    chances = 10
                    while chances > 0:
                        guess = int(input('Pick a number between 1 and 50: '))
                        if guess == number:
                            print('Great job!')
                            print('You win!')
                            again = input('Play again?(y/n) ')
                        elif guess == 0:
                            print('I said 1 to 50!')
                            print()
                        elif guess >= 51:
                            print('It cant be over 50!')
                            print()
                        
                        else:
                            nope_message = random.choice(g)
                            print(nope_message)
                            print('you have ' + str(chances - 1) + ' tries left.')
                            print(
                                )
                            
                            p = 'This is the ' + str(10 - chances) + "st time you've failed"
                            chances = chances - 1
                        if chances == 9:
                            g.append(o)
                            g.append(p)
                            
                    if chances > 0:
                        print()
                    else:
                        print('The number was ' + str(number) + '.')
                        again = input('Play again?(y/n) ')
                    if again == 'y':
                        continue
                    else:
                        break
                
            if inputl == 'times up!':
                wait = [1, 2, 3, 4, 5]
                wait_for_it = random.choice(wait)
                time.sleep(wait_for_it)
                print("Times up!")
        
            if inputl == 'examples':
                print()
                print('Notice: the output only shows the results. To see the code and the notes, see lines 128-411. ')
                mns = 1
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
                
                #1
                #prints 3 because there are three charicters in 'abc'
                a = "abc"
                print(len(a))

                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()

                #2
                #prints one letter at a time (the 'i' cn be anything as long as it is only letters and not numbers.
                for i in 'apple':
                    print(i)
    
                print()
                print('2.5:')
                print()
    
                #2.5
                #you can also do the same thing with already made variables:
                a = 'why hello there!'
                for nscs in a:
                    print(nscs)
                    #(spaces count as chericters)
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #3
                #you can also use this to print out all the things in a list:
                pbskids = [1, 2, 3, 4, 5]
                for snot in pbskids:
                    print(snot)
                    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #4
                #Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves
                x = [1,2,3]
                y = [1,2,3]
                print(x == y) # Prints out True
                print(x is y) # Prints out False
                print(x is x) # Prints out True
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #5
                #using the 'not' operation before something inverts it
                print(not False) # Prints out True
                print((not False) == (False)) # Prints out False because "not false" is the same as true and true is not the same as false
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
                
                #6
                #this is a list:
                list_example = []
                #you can add things onto your list with the list.append function.:
                list_example.append(1)
                list_example.append(2)
                list_example.append(3)
                #the first number is number 0 in the list and goes up from that. In a list with 1, 2, 3, 4, and 5, 1 is list number 0, 2 is 1, and so on.
                #if I wanted to print 1, I would do the following:
                print(list_example[0])
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #7
                #you can also do the same thing with words, for example:
                string_list = ['hello', 'world']
                string_list.append('john')
                string_list.append('henry')
                print('full string')
                print(string_list)
                print('the second word')
                print(string_list[1])
                
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #8
                #% devides and records the remainder:
                remainder = 11 % 3
                print(remainder) #prints 2 because 11/3 is 9 with a remainder of 2
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #9
                #you can add lists:
                even_numbers = [2, 4, 6, 8, 10]
                odd_numbers = [1, 3, 5, 7, 9]
                print(even_numbers + odd_numbers)
                
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #10
                #you can also form new lists inside of another function:
                print([1, 2, 3] * 3) #this prints 1, 2, 3 three times
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #11
                #you can also use %s for strings, %d for integers, %f for floating point numbers(float)(any number with a decimal)(ex: 12.83), %.<number of didgets> for floats with a fixed amount of digets to the right
                #of the dot, or %x%x for Integers in hex repersentation (lowercase/uppercase). though you have to specify the % at the end by writing % 'whatever'. You can also use this with lists.
                #this prints out 'hello john!'
                name_john = 'john'
                print('hello %s!' % name_john)

                print()
                print('11.5:')
                print()
    
                #11.5
                #you can also use multiple at the same time even if its a string(%s) and a integer(%d) which is usefull if you dont want to convert something beforehand.
                name = 'john'
                age = 24
                print('the person named %s is %d years old!' % (name, age)) #this prints 'the person namd john is 24 years old!'
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #12
                #Here is another good example of it.
                data = ("John", "Doe", 53.44)
                format_string = "Hello %s %s. Your current balance is $%s."
    
                print(format_string % data)
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #13
                #you can use variable.index(someletter) to look for the first accurence of that chericter.
                astring = 'hello world!'
                print(astring.index('l')) #this will print out 2 because it is the second letter away from the first letter.
    
                print('13.5:')
    
                #13.5
                #You can use variable.count(someletter) to count how many o them are in the string.
                print(astring.count('l')) #this will print 3 because there are 3 l's in 'hello world'.
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #14
                #you can use random.randint(1, 5) to pick a random number from 1 to five. or random.randint(1, 100) for a random number from 1 to 100, or even random.randint(50,100) for a random... oh yu get it
                print('random number from 1 to 1000: ' + str(random.randint(1, 1000)))
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
    
                #15
                #time.time takes tthe current time IN SECONDS. for example: print(time.time) would print 7:29 BUT IN SECONDS which is about 1617323579.0764525 because thats when Im writing this but it will say something differnt for u unless you are actully running this again at 7:29.
                time_total = time.time()
                print(time_total)
    
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #16
                #you can create and add to functions like this:
                def function_name():
                    print('command 1')
       
                    print('command 2')
           
                    overwatch = 1 + 2
           
                    print(overwatch)
                #functions are basicly groups of commands. so if I did function_name(), it would do all the stuff above. with me only having to write it once!
                function_name()
        
                print()
                print(str(mns) + ':')
                mns = mns + 1
                print()
        
                #17
                #you can make funtions easily customizable like this:
                def function2ishappy(filling):
                    print('piece of bread')
                    print(filling)
                    print('piece of bread')
                #so now I can make, lets say, a ham sandwhich. like this:
                function2ishappy('ham')
                #or a honey sandwhich like this:
                function2ishappy('honey')
                
                print()    
                print('17.5:')
                print()
        
                #you can also use it like this:
                def function_three_tree(number):
                    print(number)
                #this will print whatever you put in for number:
                function_three_tree(13)#this will print 13.
                
                #19
                #you can access a specific string position like this: variable_name[1] example:
                idiq = "well hello there! How do you do?"
                print(idiq[0])#this will print w, ecase that is the first thing in the string.
                #or
                print(idiq[7])#this will print l because the first l is the 8th thing in the string.
                
                print()
                print("19.25:")
                print()
                
                #19.25
                #you can also access a range of string positions like this:
                print(idiq[2:11])#this will print "ll hello " because "ll hello " is from the 3rd to the 11th thing in the string.
        
                #A more usefull use of this would be:
                if idiq[15:30] == '! How do you do?':
                    print('Access Granted')#this will print because they are the same.
                
                print()
                print("19.50:")
                print()
                
                #19.50
                #you could also emit(not include) the last number if you wan it t be from one point on:
                if idiq[15:] == '! How do you do?':
                    print('Access Granted')#this will also print because they are the same.\
        
                #this would be helpfull for sooeting like this:
                employees = ['employee1', 'employee2', 'employee3', 'employee4', 'employee5', 'employee6', 'employee7', 'employee8'
                , 'employee9', 'employee10', 'employee11', 'employee12', 'employee13', 'employee14', 'employee15', 'employee16'
                , 'employee17', 'employee18', 'employee19', 'employee20']
                random_employee = random.choice(employees)
                if random_employee[7:] == 18 or 19 or 20:
                    print("HURRAY!!! the employee is " + random_employee + "!")
        
                    print()
                    print("19.75:")
                    print()
        
                    #19.75
                    #you can do similar things with lists:
                    da_big_guy = ['Bob', '34', 'Joe', '50', 'Jeff', '29', 'Mary', '96']
                    da_big_guy_numbers = [da_big_guy[1], da_big_guy[3], da_big_guy[5], da_big_guy[7]]
                    da_big_guy_guys = [da_big_guy[0], da_big_guy[2], da_big_guy[4], da_big_guy[6]]
        
                    def person_and_age(person, age):
                        print('da very big guy is ' + person + ' and he is ' + age + ' years old!')
                    person_and_age(random.choice(da_big_guy_guys), random.choice(da_big_guy_numbers))
        
                    print()
                    print(str(mns) + ':')
                    mns = mns + 1
                    print()
        
                    #20
                    #you can print strings in upper and lower case like this:
                    alpha = 'Here Is A Sentence With Mixed Case'
                    print(alpha.upper())#this will print in all upper case
                    print(alpha.lower())#this will print it all lower case
                    
            if inputl == 'timer':
                hours = int(input('How many hours? '))
                hours = hours * 60 * 60
                while True:
                    minutes = int(input('How many minutes? '))
                    if minutes >= 60:
                        print('It has to be less than 60!')
                    else:
                        break
                minutes = minutes * 60
                while True:
                    seconds = int(input('How many seconds? '))
                    if seconds >= 60:
                        print('It has to be less than 60!')                        
                    else:
                        break
                a = (hours + minutes + seconds)
                while a >= 1:
                    print(a)
                    time.sleep(1)
                    a = a-1
                print('Done!')

                if inputl == 'leave':
                    break
            if inputl == 'leave':
                break
        if inputl =='leave':
            break
    #except:
     #   print("The system has resulted in an error. Sorry for the inconvenience")
      #  break
    finally:
        print('Goodbye!')
