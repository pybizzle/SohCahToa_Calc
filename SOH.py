#!/usr/bin/python

import math
import os

os.system('cls')

#prints info about the program to the screen for the user and begins info gathering
print("""This program will help solve RIGHT Angle Triangles

""")
#asking user for input on which formula s/he will be needed
print("""Which formula will you be using?
""")
print("Enter 1 for Sin=Opp/Hyp")
print("Enter 2 for Cos=Adj/Hyp")
print("Enter 3 for Tan=Opp/Adj")

type = int(input("""
Enter 1, 2 or 3: """))

#checks for valid input (1,2 or 3) if not will repeat the question till user inputs valid info
while(type != 1 and type != 2 and type != 3):
    type = int(input("Enter 1, 2 or 3: "))
os.system('cls')
#this starts the first loop if user asked for option 1
if(type == 1):
    print("""
    
    
You selected option #1)Sin(A)=Opp/Hyp
    
    
    """)   
    print("Enter 1 if solving for missing side length")  
    print("Enter 2 if solving for missing angle")
    type = int(input("Enter 1 or 2: "))
    while(type != 1 and type != 2):
        type = intern(input("Enter 1 or 2: "))
    if(type == 1):
        os.system('cls')
        print("""
        
        
You selected option #1)Solve for missing missing side length
        
        
        """)
        hypotenuse = float(input("Enter hypotenuse length: "))    
        angle = float(input("Enter the angle (in dec deg) opposite of side x: "))
        rad = math.radians(angle)
        opposite_length = math.sin(rad)*hypotenuse
        print "The opposite length is ", opposite_length
        print "The program is exiting"

    if(type == 2):
        os.system('cls')
        print("""
        
        
You selected option #2)Solve for missing angle
        
        
        """)     
        opposite_length = float(input("Enter the opposite side length: "))
        hypotenuse = float(input("Enter hypotenuse side length: "))
        missing_angle_deg = math.degrees(math.asin(opposite_length/hypotenuse))
        decdeg = missing_angle_deg
        degrees = int(decdeg)
        temp = 60*(decdeg - degrees)
        minutes = int(temp)
        seconds = 60*(temp - minutes)
        print "The missing angle (in decimal degrees) is ", missing_angle_deg
        print "The missing angle in DMS is ", degrees, minutes, seconds
        print "The program is exiting"        

        
elif(type == 2):
    os.system('cls')
    print("""
    
    
You selected option #2)Cos(A)=Adj/Hyp
    
    
    """)   
    print("Enter 1 if solving for missing side length")
    print("Enter 2 if solving for missing angle")
    type = int(input(""""Enter 1 or 2: """))
    while(type != 1 and type != 2):
        type = intern(input("Enter 1 or 2: "))
    if(type == 1):
        os.system('cls')
        print("""
        
        
You selected option #1)Solve for missing missing side length
        
        
        """)
        adj_length = float(input("Enter adjacent side or hypotenuse length: "))
        angle = float(input("Enter the angle (in dec deg) adjacent of side x: "))
        rad = math.radians(angle)
        hyp_length = adj_length / math.cos(rad)
        print "The opposite length is ", hyp_length
        print "The program is exiting"
        
    if(type == 2):
        os.system('cls')
        print("""
        
        
You selected option #2)Solve for missing angle
        
        
        """)
        adj_length = float(input("Enter the length of the adjacent side: "))
        hyp_length = float(input("Enter the length of the hypotenuse: "))
        missing_angle_deg = math.degrees(math.acos(adj_length / hyp_length))
        decdeg = missing_angle_deg
        degrees = int(decdeg)
        temp = 60*(decdeg - degrees)
        minutes = int(temp)
        seconds = 60*(temp - minutes)
        print "The missing angle (in decimal degrees) is ", missing_angle_deg
        print "The missing angle in DMS is ", degrees, minutes, seconds
        print "The program is exiting"        
        
elif(type == 3):
    os.system('cls')
    print("""
    
    
You selected option #3)Tan(A)=Opp/Adj
    
    
    """)
    print("Enter 1 if solving for missing side length")
    print("Enter 2 if solving for missing angle")
    type = int(input(""""Enter 1 or 2: """))
    while(type != 1 and type != 2):
        type = intern(input("Enter 1 or 2: "))
    if(type == 1):
        os.system('cls')
        print("""
        
        
You selected option #1)Solve for missing missing side length
        
        
        """)
        adj_length = float(input("Enter the  adjacent side length: "))
        known_angle = float(input("Enter the known angle (in dec deg) adjacent to the side above: "))
        rad = math.radians(known_angle)
        missing_length = math.tan(rad)*adj_length
        print "The missing adjacent length is ", missing_length
        print "The program is exiting"
        
    if(type == 2):
        os.system('cls')
        print("""
        
        
You selected option #2)Solve for missing angle
        
        
        """)
        opp_length = float(input("Enter the length of the opposite side: "))
        adj_length = float(input("Enter the length of the adjacent side: "))
        missing_angle_deg = math.degrees(math.atan(opp_length / adj_length))
        decdeg = missing_angle_deg
        degrees = int(decdeg)
        temp = 60*(decdeg - degrees)
        minutes = int(temp)
        seconds = 60*(temp - minutes)
        print "The missing angle (in decimal degrees) is ", missing_angle_deg
        print "The missing angle in DMS is ", degrees, minutes, seconds
        print "The program is exiting"        