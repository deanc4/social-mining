# Social Mining

Data mining tools for social network account analysis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

python 3

It is expected that you have a database of a specific format to run these files. The loading of data and exporting of the data can be customized to fit your integration by modifying the files.

Expected database structure for mysql:

##user

Field | Type | Description
------|------|---------------
username | VARCHAR(30) PRIMARY KEY | username
dateCreated | DATETIME | Date of account creation
largestIntervalBtwnPosts | DOUBLE | Largest number of days between a users posts

##posts

Field | Type | Description
------|------|---------------
postid | VARCHAR(10) PRIMARY KEY | unique id
username | VARCHAR(30) | username of account that created the post
subreddit | VARCHAR(1000) | (reddit) name of subreddit post was created in
title | TEXT | post title
content | TEXT | post content
points | INT(11) | (reddit) post karma
dateCreated | DATETIME | time the post was created


##comments

Field | Type | Description
------|------|---------------
commentid | VARCHAR(10) PRIMARY KEY | unique id
username | VARCHAR(30) | username of account that created the comment
subreddit | VARCHAR(1000) | (reddit) name of subreddit post was created in
content | TEXT | comment content
points | INT(11) | (reddit) comment karma
dateCreated | DATETIME | time the comment was created

## License

WTFPL
