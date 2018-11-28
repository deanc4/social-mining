#calculate the largest time interval between posts for each user.

import mysql.connector, csv, time, datetime

userPosts = {}
database = mysql.connector.connect(user='username', password='password', host='hostname', database='databaseName')
cursor = database.cursor()

def mapUsersAndDates():

    cursor.execute("SELECT username, dateCreated FROM posts;")
    postResult = cursor.fetchall()

    for row in postResult:

        username = row[0]
        postDate = row[1]
        
        if username not in userPosts:
            userPosts[username] = [postDate]
        else:
            userPosts[username].append(postDate)

def sortDates():
    for username, postList in userPosts.items():
        
        postList.sort()

# calculates the largest time difference between posts. Defaults to zero if only one post.
def calculateLargestTimeDifference():
    for username, postList in userPosts.items():
       
        maximum = datetime.timedelta(0,0,0)
        previous = postList[0]
        
        for date in postList:
            delta = date - previous
            previous = date
            
            if delta > maximum:
                maximum = delta
        
        userPosts[username] = maximum

def pushToDatabase():
    for username, time in userPosts.items():
        days = time.days
        
        try:
            cursor.execute("""UPDATE user SET largestIntervalBwtnPosts=%s WHERE username=%s""", (days, username))
            database.commit()
        
        except Exception as e:
            print("error on " + username + " " + str(days) + "\n" + str(e))
    
    database.close()

mapUsersAndDates()
sortDates()
calculateLargestTimeDifference()
pushToDatabase()
