

Task 1: 

1) The repo consists of basic Source code to Create a Container Registry and a Docker image , pushed as it is being Provisioned.



2) The Things I would also want to Include are Unit Tests.



3) Integration tests could be Covered by Python, to check if Provisioning has been successful, in these tests, I would include a test to see, if the linux image was available, the region was the chosen region etc etc



4) The other bit I would have liked to add, but would not be doing right now because I have not got the time is checking validation against every single field to see, if it has the right prefix etc etc, more like a static lint



5) Its a good practice to ensure the state files lives in a Azure Global bucket, which I will be adding within the code base. 

