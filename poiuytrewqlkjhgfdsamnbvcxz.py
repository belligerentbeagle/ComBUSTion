from microbit import *
time = 0
phone = 0 
total_time = 0
def turn_motor():     
    pin16.write_analog(512)  #512 is the angle
   
while True:
    if pin0.read_analog() == 2:  #A is 15 minutes
        time += 15
        display.scroll(str(time))
    elif pin0.read_analog() == 53:
        time += 30
        display.scroll(str(time))
    elif pin0.read_analog() == 98:
        time += 60
        display.scroll(str(time))
    elif pin0.read_analog() == 140:
        time += 120
        display.scroll(str(time))
    elif pin0.read_analog() == 545:
        time = 0
        display.scroll(str(time))
 
        
    if button_a.is_pressed(): 
        turn_motor() 
        if pin1.read_analog() >700:
            phone = 1
            time_irl = time * 60 * 1000
            total_time += time
            sleep(time_irl) #start timer only after it has been locked, time is in millisecs
            pin16.write_analog(0) #after timer ends, box is unlocked.
        elif pin1.read_analog() <700:
            phone = 0         #makes sure phone is inside the box before timer starts
            display.scroll("Phone not in")
            time = 0
            
    if button_b.is_pressed():
        display.show(total_time)
         
        
            
        
       

        