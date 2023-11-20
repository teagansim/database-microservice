# database-microservice
A small microservice to take a location and branch, and return availability.

To request service from microservice, open "branch-booking.txt", which should be located in the same folder as the microservice.
On the first line, write a location, and if desired, a branch number after a comma, with no space.
Examples: "seattle", or "portland,3"
After writing to file, close file.

To receive response from microservice, open "branch-booking.txt" after waiting 1 second or more since the request was written to file.
It is to wait for response in a loop, as the response may take longer than 1 second to be given.
Read the top line of the file to receive your response.
Close the file.

Basic use:
To search for the first availability at a location, write a location with no branch number.
To make an appointment at a specific branch, include the location and branch number.

Functionality:
The microservice will open the branch-booking text file and read the contents.
If a proper request has been made, it will begin its lookup.
Service will check if location is in the databse.
If no location found, it will resoind with "invalid"
If location is found, it will check if there is a branch number in the request.
If no branch number given, it will find the location in the database, and respond with the first branch number with availability.
If branch number is given, it will search for that branch in the database.
If the number at that branch is 0, it will respond with "invalid".
If the number is greater than 0, it will subtract 1 and return "valid".
If the call is invalid, the response should be "invalid"
In the case other errors occur, or functionality is not as expected, please contact the developer.

Below is a link to a diagram illustrating the communication between microservice and client:
https://imgur.com/a/wIY4VWP
