from pynput import mouse
from pynput import keyboard
from random import random
import threading
import time
from time import time as timer
from pydub import AudioSegment
from pydub.playback import play

result = None


#result_available = threading.Event()
song = AudioSegment.from_wav("sound.wav")

def twentyfiveminwait():
    t_end = time.time() + 1 #60*20 # TIME TO WAIT BEFORE RUNNING THE CODE
    while time.time() < t_end:
        print("wait 25 minutes")

# working during a minute




def eye_movement():


    print("60 second loop")
    movecounter = []
    
    global global_mov
    global global_t_diff
    global result
    global global_mov_27  
    global global_t_diff_27
    global n_times



    if len(global_mov) is 0:

        print("we are in a mint loop")

        t_end = time.time() + 60
        t1 = time.time()

        while time.time() < t_end:
            with mouse.Events() as events:
                for event in events:
                    movecounter.append("1")

                    print('Received event {}'.format(event) + ' eyes movement: ' + str(len(movecounter)))
               
                
                    if len(movecounter) > 27:

                        result = len(movecounter)
                        t2 = time.time()


                        global_mov_27.append(result)
    
                        global_t_diff_27.append(int(t2-t1))

                        global_mov.append(len(global_mov_27))
                        global_t_diff.append(int(t2-t1))

                    
                        movecounter = []

                        print("first condition satisfied")
                        print("movements so far:{}".format(global_mov_27))
                        print("time difference so far:{}".format(global_t_diff_27))
                        print("loop summary {}{}".format(global_mov_sum, global_t_sum))

                        global_mov_27 = []
                        global_t_diff_27 = []
                        print('Total eye movement higher that 27, moving to the alternative loop') # EYE MOVEMENTS PER MINUTE


                    else:

                    
                        t3 = time.time()  #  for getting summary and time of each movement
                    
                        global_mov_sum.append(len(movecounter))
                        global_t_sum.append(int(t3 - t1))
                        break



                    break


    else:
        print("we are in alternative loop")
        t_end = time.time() + 60
        t1 = time.time()

        while time.time() < t_end:
            with mouse.Events() as events:
                for event in events:
                    movecounter.append("1")

                    print('Received event {}'.format(event) + ' eyes movement: ' + str(len(movecounter)))
               
                    
                
                    if len(movecounter) > 7:

                        result = len(movecounter)
                        t2 = time.time()


                        global_mov.append(result)
    	
                        global_t_diff.append(int(t2-t1))


                        if sum(global_t_diff) > 80:

                            global one_time
                            n_times.append(1)

                            print("we are in execution loop")

                            print("the stimulus has been given this number of times: {}".format(len(n_times)))

                            global_mov = []
                            global_t_diff = []
                            


                            print('ntimes this loop:', one_time)


                            if one_time == 1:

                                one_time = 0
                                if len(n_times) <= 5: # NUMBER OF TIMES THE SONG WILL BE PLAYED
                                    print("the song is played")
                                    play(song)
                                    movecounter = []
                                    

                                else:
                                    break
                            else:
                                break

                    else:

                    
                        t3 = time.time()  #  for getting summary and time of each movement
                    
                        global_mov_sum.append(len(movecounter))
                        global_t_sum.append(int(t3 - t1))

                        global_mov = []

                        break



                    break



#def eye_movement():
#    movecounter = []
#    while len(movecounter) < 10:
#        with mouse.Events() as events:
#            for event in events:
#                movecounter.append("1")
#                print('Received event {}'.format(event) + ' eyes movement: ' + str(len(movecounter)))
#                if len(movecounter) > 10:
#                    print('Total eye movement higher that 100')
#                    global result
#                    result = len(movecounter)
#                    play(song)
#                    break


def main():

    twentyfiveminwait()

    global n_times
    global global_mov
    global global_t_diff
    global global_mov_sum
    global global_t_sum
    global global_mov_27
    global global_t_diff_27


    n_times = []
    global_mov = []
    global_t_diff = [] 
    global_mov_sum = []
    global_t_sum = [] 
    global_mov_27 = []
    global_t_diff_27 = []
 
    for i in range(180):

        global one_time # for given satisfied conditions the stimulus cannot be given more than once
    
        one_time = 1

        print("we are in loop {}".format(i+1))
        eye_movement()
        print("Summary for this loop")
        print("movements acc: {}".format(global_mov_sum))
        print("time acc: {}".format(global_t_sum))
        global_mov_sum = []
        global_t_sum = []


	
    #thread = threading.Thread(target=eye_movement)
    #thread.start()

    # wait here for the result to be available before continuing
    #result_available.wait()
    #thread.join()

    print('The result is', result)

if __name__ == '__main__':
    main()
