try:
    from auth import auth
except:
    with open("auth.py","w") as a:
        a.write("auth = ('<username>','<password>')")
        print("Add login info to auth.py!")
    quit()

import trainInfomation
import pygame
import datetime
import threading
import time

def firstLetterVowelDetect(string):
    if string[0].lower() in ['a','e','i','o','u']:
        return True
    else:
        return False

def updateInfomation(code):
    global station
    while True:
        print("Updating")
        station = trainInfomation.station(code)
        if stopThread:
            break
        time.sleep(10)

def TrainInfo(station):
    if firstLetterVowelDetect(station.trains[0].operator):
        scrollText = f"This is an {station.trains[0].operator} service to {station.trains[0].destination}"
    else:
        scrollText = f"This is a {station.trains[0].operator} service to {station.trains[0].destination}"
    scrollText = f"{scrollText}              Calling at: "
    for i in station.trains[0].callingAt:
        if i == station.trains[0].callingAt[-1]:
            scrollText = f"{scrollText}and {i}"
        else:
            scrollText = f"{scrollText}{i}, "
    return scrollText

print("Powered by RealTimeTrains API (https://api.rtt.io/)")
code = input("Type in a station code: ")
print("Please wait")
station = trainInfomation.station(code)
shownStation = station

pygame.init()
clock = pygame.time.Clock()  # Clock is capital C
height = 320
width = 1200

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption(f'Train Infomation: {station.inputStaion} - {code.upper()}')
pygame.display.update()

font = pygame.font.SysFont(None, 75)

scrollTextAmount = 0
updateThread = threading.Thread(target=updateInfomation, args=(code,))
stopThread = False
updateThread.start()
while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            stopThread = True
            quit()
    gameDisplay.fill((0,0,0))

    TrainOrderIndicator1 = font.render("1st", True, (255, 165, 0))
    gameDisplay.blit(TrainOrderIndicator1, (20, 20))
    TrainTimeIndicator1 = font.render(f"{shownStation.trains[0].time}", True, (255, 165, 0))
    gameDisplay.blit(TrainTimeIndicator1, (140, 20))
    TrainDestinationIndicator1 = font.render(f"{shownStation.trains[0].destination}", True, (255, 165, 0))
    gameDisplay.blit(TrainDestinationIndicator1, (320, 20))
    TrainEstimation1 = font.render(f"{shownStation.trains[0].getExpectedInfo()}", True, (255, 165, 0))
    gameDisplay.blit(TrainEstimation1, (width - TrainEstimation1.get_rect().width-20, 20))
    TrainInfomation1 = font.render(f"{TrainInfo(shownStation)}", True, (255, 165, 0))
    gameDisplay.blit(TrainInfomation1, (scrollTextAmount, 100))
    scrollTextAmount -= 5
    if scrollTextAmount < (TrainInfomation1.get_rect().width+5)*-1:
        scrollTextAmount = width
        shownStation = station
    
    TrainOrderIndicator2 = font.render("2nd", True, (255, 165, 0))
    gameDisplay.blit(TrainOrderIndicator2, (20, 180))
    TrainTimeIndicator2 = font.render(f"{shownStation.trains[1].time}", True, (255, 165, 0))
    gameDisplay.blit(TrainTimeIndicator2, (140, 180))
    TrainDestinationIndicator2 = font.render(f"{shownStation.trains[1].destination}", True, (255, 165, 0))
    gameDisplay.blit(TrainDestinationIndicator2, (320, 180))
    TrainEstimation2 = font.render(f"{shownStation.trains[1].getExpectedInfo()}", True, (255, 165, 0))
    gameDisplay.blit(TrainEstimation2, (width - TrainEstimation2.get_rect().width-20, 180))

    CurrentTime = font.render(f"{current_time}", True, (255, 165, 0))
    gameDisplay.blit(CurrentTime, ((width / 2) - (CurrentTime.get_rect().width / 2), height - CurrentTime.get_rect().height-20))

    clock.tick(120)
    pygame.display.update()