"""
Very Beginner Python Project by Kylie Ying
Madlibs using string concatenation

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""
# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

""" 
[DATE]

[ORGANIZATION]

[ADDRESS]

Dear Sir,

As per our recent conversation, please accept this letter as a formal request for your permission to hold a “mock crash” at [NAME OF SCHOOL] on [DATE OF MOCK CRASH]. The initiative will educate students about the positive role that seat belts play in trac crashes and about the consequences of drinking and driving.

Once your approval has been obtained, we will be arranging for a wrecked vehicle to be towed to the school on [DATE OF MOCK CRASH]. Please note that we will be taking care of all other details pertaining to the setup of the “mock crash” as well.

It is our understanding that you will ensure that this does not contravene any guidelines set by our school board. If you have any questions or wish to meet to discuss the “crash” in further detail, please contact me or our sponsor teacher, [NAME OF SPONSOR TEACHER].

Thank you for allowing us this opportunity to help get our very important traffic safety message across to our fellow
students.

Sincerely,
[NAME OF STUDENT COUNCIL REPRESENTATIVE]
"""
date = input("DATE: ")
ORGANIZATION = input("ORGANIZATION: ")
ADDRESS = input("ADDRESS: ")
NAME_OF_SCHOOL = input("NAME OF SCHOOL: ")
DATE_OF_MOCK_CRASH = input("DATE OF MOCK CRASH: ")
NAME_OF_SPONSOR_TEACHER = input("NAME OF SPONSOR TEACHER: ")
NAME_OF_STUDENT_COUNCIL_REPRESENTATIVE = input("NAME OF STUDENT COUNCIL REPRESENTATIVE: ")

f = open("letter.txt", "w")
f.write(f""" 
{date}

{ORGANIZATION}

{ADDRESS}

Dear Sir,

As per our recent conversation, please accept this letter as a formal request for your permission to hold a mock crash at {NAME_OF_SCHOOL} on {DATE_OF_MOCK_CRASH}. The initiative will educate students about the positive role that seat belts play in trac crashes and about the consequences of drinking and driving.

Once your approval has been obtained, we will be arranging for a wrecked vehicle to be towed to the school on {DATE_OF_MOCK_CRASH}. Please note that we will be taking care of all other details pertaining to the setup of the “mock crash” as well.

It is our understanding that you will ensure that this does not contravene any guidelines set by our school board. If you have any questions or wish to meet to discuss the “crash” in further detail, please contact me or our sponsor teacher, {NAME_OF_SPONSOR_TEACHER}.

Thank you for allowing us this opportunity to help get our very important traffic safety message across to our fellow
students.

Sincerely,
{NAME_OF_STUDENT_COUNCIL_REPRESENTATIVE}""")
f.close()