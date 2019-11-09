import time
#import playsound vms
def main(bpm = 60, bpb = 4):
    sleep = 60.0 / bpm
    counter = 0
    while True:
        counter += 1
        if counter % bpb:
            print("tick")
        else:
            print("TICK") #siia saab panna playsound-iga metronoomi mp3 käima
        time.sleep(sleep)
        
main()