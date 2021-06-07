"""
file: Brute Force
Description: functions
Created: 23/12/2020.
Updated: 20/1/2021.
Authors: Asia Benyadilok
"""

from functools import reduce
import hashlib
import random
import itertools
import time

#method: bruteForce
#parameters: String hashInput
#Description: called when need to brute force passwords that are from a to 9 with maximum of 6 characters
def bruteForce(hashInput):

    #initialize variables
    seed = 'abcdefghijklmnopqrstuvwxyz0123456789'
    randomSeed = "".join(random.sample(seed,len(seed)))
    attempts = 0
    solved = False

    # change characters to ascii code
    mapAscii = list(map(ord, randomSeed))

    #set start time
    startTime = time.time()

    #generate all possible combination from 1 to 6 characters
    for i in range(1,7):
        for comAsCII in itertools.product(mapAscii, repeat= i):

            #map ascii code back to characters
            mapChr = map(chr, comAsCII)

            #get combination of string generated
            comString = reduce(lambda x, y: x+y, mapChr)

            #hash the combination with SHA1
            comHash = hashlib.sha1(comString.encode('utf-8')).hexdigest()

            # compare hash with input
            if (comHash == hashInput):

                #set end time
                endTime = str(time.time() - startTime)

                #show result
                print('\nInput sha 1 hash: ' + hashInput)
                print('Password: ' + comString)
                print('Attempts: ',attempts)
                print('time used: ', endTime ,' sec')
                solved = True
                break

            attempts += 1

        if solved == True:
            break

#method: bruteForceBCH
#parameters: String hashInput
#Description: called when need to brute force passwords that are valid BCH(10,6)
def bruteForceBCH(hashInput):

    #initialize variables
    seed ='0123456789'
    randomSeed = "".join(random.sample(seed, len(seed)))
    attempts = 0

    # change characters to ascii code
    mapAscii = list(map(ord, randomSeed))

    #initailize matrix for calculating BCH(10,6)
    d7m = [4, 10, 9, 2, 1, 7]
    d8m = [7, 8, 7, 1, 9, 6]
    d9m = [9, 1, 7, 8, 7, 7]
    d10m = [1, 2, 9, 10, 4, 1]

    #set start time
    startTime = time.time()

    #generate all possible of 6 digits
    for comAsCII in itertools.product(mapAscii, repeat=6):

        # map ascii code back to characters
        mapChr = map(chr, comAsCII)

        # get combination of string generated
        comString = reduce(lambda x, y: x + y, mapChr)

        d7 = 0
        d8 = 0
        d9 = 0
        d10 = 0

        #calculating 4 digits for BCH(10,6)
        for i in range(6):
            d7 += (d7m[i] * int(comString[i]))
            d8 += (d8m[i] * int(comString[i]))
            d9 += (d9m[i] * int(comString[i]))
            d10 += (d10m[i] * int(comString[i]))

            if i == 5:
                d7 %= 11
                d8 %= 11
                d9 %= 11
                d10 %= 11

        #check for a valid BCH(10,6)
        if (d7 < 10 and d8< 10 and d9< 10 and d10< 10):
            comString = comString+str(d7)+str(d8)+str(d9)+str(d10)

            #if it is a valid BCH(10,6) then hash it
            comHash = hashlib.sha1(comString.encode('utf-8')).hexdigest()

            #compare hash with input
            if (comHash == hashInput):

                #set end time
                endTime = str(time.time() - startTime)

                #show result
                print('\nInput sha 1 hash: ' + hashInput)
                print('Password: ' + comString)
                print('Attempts: ', attempts)
                print('time used: ', endTime, ' sec')
                break

        attempts += 1


#sample to run program
bruteForce("6ef80072f39071d4118a6e7890e209d4dd07e504")
bruteForceBCH("5b8f495b7f02b62eb228c5dbece7c2f81b60b9a3")