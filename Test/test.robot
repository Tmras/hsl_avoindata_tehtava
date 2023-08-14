*** Settings ***
Library   resources.py

*** Test Cases ***
Test Getting Realtime Data
    [Documentation]     Checks if realtime data is succesfully returned from the client
    check realtime data received for id    1

Test Getting Realtime Data For Nonexisting Id
    [Documentation]     Checks that message is returned informnin that hte desired id does not exist the hsl api returns nothing at this point
    check error message received for nonexisting id    2    Facility with id: 2 does not exist

Test Getting Realtime Data With Wrong Id Type
    [Documentation]     Checks that api returns message about non existing id is when the id is letters.
    check error message received for nonexisting id    asdfg    Facility with id: asdfg does not exist
    
Test If Diagram Window Opens
    [Documentation]     Checks that api returns 200 and diagram is opened. Currently manual check and closing of the diagram is required from the user.
    get saved data    1
    get saved data    755

Test If Diagram Window Opens
    [Documentation]     Checks that empty diagram is successfully opened when the id is nonexisting. Currently user is reuired to confirm and close the diagram manually.
    get saved data    asdfg