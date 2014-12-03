#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

import random

def hello(phenny, input): 
<<<<<<< HEAD
    greeting = random.choice(('Hi', 'Hey', 'Hello'))
    punctuation = random.choice(('', '!'))
    phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey) $nickname[ \t]*$'
=======
    global temporaryMessage
    global emptyHellos
    global greetings

    nickname = phenny.nick
    greeting = random.choice(greetings)
    if not re.search(nickname, input) and temporaryMessage is not None:
        punctuation = random.choice(('.', '!', ';'))
        phenny.say(greeting + ' ' + input.nick + punctuation +temporaryMessage)
        countGuest(phenny, input.nick)
    elif emptyHellos:
        punctuation = random.choice(('', '!'))
        phenny.say(greeting + ' ' + input.nick + punctuation)
    elif re.search(nickname, input):
        punctuation = random.choice(('', '!'))
        phenny.say(greeting + ' ' + input.nick + punctuation)


#hello.rule = r'(?i)(hi|hello|hey|what\'s kickin[\'g]*|how you been|what\'s (.*)good(.*)|top o[\'f]* the mornin[\'g]*|what\'s hangin[\'g]*|yo|in the hood|in da hood|kaixo|zer moduz|с[әа]л[еао]м|wb) $nickname[ \t]*$'
#strings = "(?i)(hi|hello|hey|what\'s kickin[\'g]*|how you been|what\'s (.*)good(.*)|top o[\'f]* the mornin[\'g]*|what\'s hangin[\'g]*|yo|in the hood|in da hood|kaixo|zer moduz|с[әа]л[еао]м|s[ae]l[ao]m|wb)"
hello.rule = r'(?:$nickname[,:]* )?(?i)(hi|hello|hey|what\'s kickin[\'g]*|how you been|what\'s (.*)good(.*)|what\'s up|sup|(?:top o[\'f]* the )?mornin[\'g]*|what\'s hangin[\'g]*|yo|in the hood|in da hood|kaixo|zer moduz|с[әа]л[еао]м|s[ae]l[ao]m|wb|mitä kuuluu|როგორა ხარ|ինչպե՞ս ես|сайн байна уу|कैसे हो|como vai|nasılsın(?:ız)?)(?:[,]* $nickname)?[ \t!\.\?]*$'
>>>>>>> 508b470... Fixed .queue display by showing a list of queues when none is specified

def interjection(phenny, input): 
    phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False

if __name__ == '__main__': 
    print(__doc__.strip())
