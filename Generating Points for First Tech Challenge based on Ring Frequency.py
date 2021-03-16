from random import randint
scores = []
ringtimings = []
pastring = 0
for x in range(0,20):
    tempring = []
    time = 90
    sum = 165
    rings = 0
    while time > 0:
        random = randint(0,100)
        if random <= 10:
            ring = randint(45,60)

        elif random <= 30:
            ring = randint(35,40)
        elif random <= 90:
            ring = randint(15, 35)
        elif random <= 100:
            ring = randint(5, 15)

        if pastring != 0:
            if pastring == ring:
                continue
        tempring.append(ring)
        #print("ring time:" + str(ring))
        #$if time - ring < 0:
           # if time > 15:
               # break
        time += -ring
        #print("time: " + str(time))
        if randint(1,100) <= 5:
            sum += 12
        else:
            sum += 18
        pastring = ring
        rings += 1
    scores.append(sum)
    ringtimings.append(tempring)
scores.sort(reverse=True)
for o in range(0, 7):
    print("Generated score " + str(o+1) + " : "  + str(scores[o]))
    print("Ring timings " + str(o + 1) + " : " + str(ringtimings[o]))

