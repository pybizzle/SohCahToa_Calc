#!/usr/bin/python
# -- coding: cp1252 -- 
 
    
import math
import os
import webbrowser


new = 2;

image = "right_tri.jpg"

webbrowser.open(image, new=new);


try:    
       
    os.system('clear')
    
    #prints info about the program to the screen for the user and begins info gathering
    print("""This program will help solve RIGHT Angle Triangles
    
    """)
    #asking user for input on which formula s/he will be needed
    print("""Which formula will you be using?
    """)
    print("Enter 1 for Sin=Opp/Hyp")
    print("Enter 2 for Cos=Adj/Hyp")
    print("Enter 3 for Tan=Opp/Adj")
    print("")
    print("Press 'q' at anytime to quit")
    
    q = os.system('exit')
    
    user_input = int(input("""
Enter 1, 2 or 3: """))
    
    #checks for valid input (1,2 or 3) if not will repeat the question till user inputs valid info
    while(user_input != 1 and user_input != 2 and user_input != 3 and user_input != q):
        user_input = int(input("Enter 1, 2 or 3: "))
    os.system('clear')
    #this starts the first loop if user asked for option 1
    if(user_input == 1):
        print("""
        
        
You selected option #1) Sin(A)=Opp/Hyp
        
        
        """)   
        print("Enter 1 if solving for missing side length") + ".\n" 
        print("Enter 2 if solving for missing angle") + ".\n"
        user_input = int(input("Enter 1 or 2: "))
        while(user_input != 1 and user_input != 2 and user_input != q):
            user_input = int(input("Enter 1 or 2: "))
        if(user_input == 1):
            os.system('clear')
            print("""
            
            
You selected option #1) Solve for missing missing side length

(**NOTE: The known Angle will be "Angle (A)" and the unsolved angle will be "Angle (B).**)
            
            
            """)
            hyp_known = float(input("Enter hypotenuse side (c) length: "))    
            angle_known = float(input("Enter the known angle (A) (in Dec. Deg.) opposite of side (X): "))
            angle_unknown = 180 - 90 - angle_known
            rad_known = math.radians(angle_known)
            opp_length = math.sin(rad_known)*hyp_known
            degrees = int(angle_unknown)
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            temp = 60*(angle_unknown - degrees)
            minutes = int(temp)
            seconds = 60*(temp - minutes)
            adj_length = math.sqrt((hyp_known**2)-(opp_length**2))
            os.system('clear')
            print """
            
The OPPOSITE side (b) length is """, opp_length
            print("")
            print "Angle (B) in Dec. Deg. is ", angle_unknown
            print("")
            print "Angle (B) in DDMMSS is ", degrees,deg_sym, minutes,min_sym, seconds,sec_sym
            print("")
            print "The ADJACENT side (b) length is ", adj_length
            print("")
            print "And of course EVERY Right Angle Triangle has one 90° angle, and all three side are equal to 180 so..."
            print("")
            print 'If' , str(angle_unknown), '+',  str(angle_known), '+', + 90, '=', str(angle_unknown + angle_known + 90), '° than our triangle is correct!'
            print("")
            print "The program is exiting"
    
        if(user_input == 2):
            os.system('clear')
            print("""

You selected option #2) Solve for missing angle
            
(**NOTE: The Angle you're solving for is "Angle (A)" and the (other) unsolved angle will be "Angle (B).**)        
            """)

            #user input 
            opp_known = float(input("Enter the opposite side (a) length: "))
            hyp_known = float(input("Enter hypotenuse side (c) length: "))
            #doing the math
            angle_a = math.degrees(math.asin(opp_known/hyp_known))
            adj_length = math.sqrt((hyp_known**2)-(opp_known**2))
            #solving for other angle
            angle_b = 180 - (angle_a + 90)
            #converting decdeg to DDMMSS
            degrees_a = int(angle_a)
            temp_a = 60*(angle_a - degrees_a)
            minutes_a = int(temp_a)
            seconds_a = 60*(temp_a - minutes_a)
            degrees_b = int(angle_b)
            temp_b = 60*(angle_b - degrees_b)
            minutes_b = int(temp_b)
            seconds_b = 60*(temp_b - minutes_b)
            #saving symbols as variables to use in strings
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            #printing the results to the screen
            os.system('clear')
            print "Angle (A) in decimal degrees is ", angle_a
            print("")
            print "Angle (A) in DDMMSS is ", degrees_a,deg_sym, minutes_a,min_sym, seconds_a,sec_sym
            print("")
            print "The ADJACENT side (b) length is ", adj_length
            print("")
            print "And of course EVERY Right Angle Triangle has one 90° angle, and all three side are equal to 180 so..."
            print("")
            print 'If' , 180, '-', '(',str(angle_a), '+', + 90,')', '=', 180 - (angle_a + 90),'°'
            print("")
            print "Angle (B) in decimal degrees is ", angle_b,'°'
            print("")
            print "Angle (B) in DDMMSS is ",  degrees_b,deg_sym, minutes_b,min_sym, seconds_b,sec_sym
            print("")
            print "Thank You, Come Again!!"
    
        elif(user_input == q):
            os.system('exit')   
                 
    elif(user_input == 2):
        os.system('clear')
        print("""
        
        
You selected option #2) Cos(A)=Adj/Hyp
        
        
        """)   
        print("Enter 1 if solving for missing side length") + ".\n"
        print("Enter 2 if solving for missing angle") + ".\n"
        user_input = int(input("""Enter 1 or 2: """))
        while(user_input != 1 and user_input != 2 and user_input != q):
            user_input = int(input("Enter 1 or 2: "))
        if(user_input == 1):
            os.system('clear')
            print("""
            
            
You selected option #1) Solve for missing missing side length
(**NOTE: The known Angle will be "Angle (A)" and the unsolved angle will be "Angle (B).**)            
            
            """)
            #user input
            adj_length = float(input("Enter adjacent (a) side length: "))
            angle_a = float(input("Enter the known angle (A) (in Dec. Deg.) adjacent to Angle (A): "))
            #converting decdeg to radians for calculations
            rad_a = math.radians(angle_a)
            #doing the calculations
            hyp_length = adj_length / math.cos(rad_a)
            #solving for other angle
            angle_b = 180 - (angle_a + 90)
            #6converting decdeg to DDMMSS
            degrees_a = int(angle_a)
            temp_a = 60*(angle_a - degrees_a)
            minutes_a = int(temp_a)
            seconds_a = 60*(temp_a - minutes_a)
            degrees_b = int(angle_b)
            temp_b = 60*(angle_b - degrees_b)
            minutes_b = int(temp_b)
            seconds_b = 60*(temp_b - minutes_b)
            #saving symbols as variables to use in strings
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            #printing the results to the screen
            os.system('clear')
            print "The opposite side (b) length is ", hyp_length
            print("")
            print "Angle (A) in decimal degrees is ", angle_a
            print("")
            print "Angle (A) in DDMMSS is ", degrees_a,deg_sym, minutes_a,min_sym, seconds_a,sec_sym
            print("")
            print "Angle (B) in decimal degrees is ", angle_b,'°'
            print("")
            print "Angle (B) in DDMMSS is ",  degrees_b,deg_sym, minutes_b,min_sym, seconds_b,sec_sym
            print("")
            print "The program is exiting.."
            
        if(user_input == 2):
            os.system('clear')
            print("""
            
            
You selected option #2) Solve for missing angle
            
            
            """)
            adj_length = float(input("Enter the adjacent side (b) lenght: "))
            hyp_length = float(input("Enter the hypotenuse side (c) lenght: "))
            #doing the calculations 
            angle_a = math.degrees(math.acos(adj_length / hyp_length))
            #solving for other angle
            angle_b = 180 - (angle_a + 90)     
            #solving for other length
            opp_length = math.sqrt(hyp_length**2-adj_length**2) 
            #converting decdeg to DDMMSS
            degrees_a = int(angle_a)
            temp_a = 60*(angle_a - degrees_a)
            minutes_a = int(temp_a)
            seconds_a = 60*(temp_a - minutes_a)
            degrees_b = int(angle_b)
            temp_b = 60*(angle_b - degrees_b)
            minutes_b = int(temp_b)
            seconds_b = 60*(temp_b - minutes_b)
            #saving symbols as variables to use in strings
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            #printing the results to the screen
            os.system('clear')
            print "Angle (A), in decimal degrees is ", angle_a
            print("")
            print "Angle (A), in DDMMSS is ", degrees_a,deg_sym, minutes_a,min_sym, seconds_a,sec_sym
            print("")
            print "The OPPOSITE side (a) length is ", opp_length
            print("")
            print "And if all right triangles have 3 sides that equal 180 and have one 90 angle, then to solve for Angle (B)..."
            print("")
            print  180, '-', '(',str(angle_a), '+', + 90,')', '=', 180 - (angle_a + 90),'°'
            print("")
            print "Angle (B) in decimal degrees is ", angle_b,'°'
            print("")
            print "Angle (B) in DDMMSS is ",  degrees_b,deg_sym, minutes_b,min_sym, seconds_b,sec_sym
            print("")
            print "The program is exiting.."
    
        elif(user_input == q):
            os.system('exit')
    
    elif(user_input == 3):
        os.system('clear')
        print("""
        
        
You selected option #3) Tan(A)=Opp/Adj
        
        
        """)
        print("Enter 1 if solving for missing side length") + ".\n"
        print("Enter 2 if solving for missing angle") + ".\n"
        user_input = int(input("""Enter 1 or 2: """))
        while(user_input != 1 and user_input != 2 and user_input != q):
            user_input = int(input("Enter 1 or 2: "))
        if(user_input == 1):
            os.system('clear')
            print("""
            
            
You selected option #1)Solve for missing missing side length
            
            
            """)
            #asking for user input
            adj_length = float(input("Enter the  adjacent side (a) length: "))
            angle_b = float(input("Enter the known angle (in dec deg) Angle (B): "))
            #doing the calculations
            rad_b = math.radians(angle_b)
            missing_length = math.tan(rad_b)*adj_length
            #saving symbols as variables to use in strings
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            #calculating the missing hypotenuse lenght
            hyp_length = math.sqrt(adj_length**2 + missing_length**2)
            #solving for other angle
            angle_a = 180 - (angle_b + 90)
            #converting decdeg to DDMMSS
            degrees_a = int(angle_a)
            temp_a = 60*(angle_a - degrees_a)
            minutes_a = int(temp_a)
            seconds_a = 60*(temp_a - minutes_a)
            degrees_b = int(angle_b)
            temp_b = 60*(angle_b - degrees_b)
            minutes_b = int(temp_b)
            seconds_b = 60*(temp_b - minutes_b)
            os.system('clear')
            print("")
            print "The missing OPPOSITE side (a) length is ", missing_length
            print("")
            print "The HYPOTENUSE side (c) length is ", hyp_length
            print("")
            print "The other/unknown Angle (A) in DDMMSS is ", degrees_a,deg_sym, minutes_a,min_sym, seconds_a,sec_sym
            print("")
            print "The other/unknown Angle (A) in Decimal Degrees is ", angle_a
            print("")
            print "The program is exiting"
            
        if(user_input == 2):
            os.system('clear')
            print("""
            
            
You selected option #2)Solve for missing angle
            
            
            """)
            #asking for user input
            opp_length = float(input("Enter the length of the opposite side (a): "))
            adj_length = float(input("Enter the length of the adjacent side (b): "))
            #doing the calculations
            angle_b = math.degrees(math.atan(opp_length / adj_length))
            #calculating the missing hypotenuse side length
            hyp_length = math.sqrt(adj_length**2 + opp_length**2)
            #saving symbols as variables to use in strings
            deg_sym = '°'
            min_sym = "'"
            sec_sym = '"'
            #solving for other angle
            angle_a = 180 - (angle_b + 90)
            #converting decdeg to DDMMSS
            degrees_a = int(angle_a)
            temp_a = 60*(angle_a - degrees_a)
            minutes_a = int(temp_a)
            seconds_a = 60*(temp_a - minutes_a)
            degrees_b = int(angle_b)
            temp_b = 60*(angle_b - degrees_b)
            minutes_b = int(temp_b)
            seconds_b = 60*(temp_b - minutes_b)
            os.system('clear')
            print "Angle (A) in Decimal Degrees is ", degrees_a, deg_sym, minutes_a, min_sym, seconds_a, sec_sym
            print("")
            print "Angle (A) in DDMMSS is ", angle_a
            print("")
            print "Angle (B) in Decimal Degrees is ", angle_b
            print("")
            print "Angle (B) in DDMMSS is ", degrees_b,deg_sym, minutes_b,min_sym, seconds_b,sec_sym
            print("")
            print "The HYPOTENUSE side (c) length is ", hyp_length
            print("")
            print "The program is exiting"    
            
       
            
        elif(user_input == q):
            os.system('exit')
              
    elif(user_input == q):
        os.system('exit')

except Exception, e:
    print str(e) + " - please try again"