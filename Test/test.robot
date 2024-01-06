*** Settings ***
Library   resources.py

*** Test Cases ***
Test Getting Realtime Data
    [Documentation]     Checks if realtime data is succesfully returned from the client
    check realtime data received for id    ${1}

Test Getting Realtime Data For Nonexisting Id
    [Documentation]     Checks that message is returned informing that the desired id does not exist the hsl api
    check error message received for nonexisting id    ${2}    "Facility with id: 2 does not exist"

Test Getting Realtime Data With Wrong Id Type
    [Documentation]     Checks that api returns message about non existing id is when the id is letters.
    check error message received for nonexisting id    asdf    "Facility with id: asdf does not exist"
    
Test If Diagram Window Opens
    [Documentation]     Checks that api returns 200 and diagram is opened. Currently check by user is needed.
    get saved data    1
    get saved data    755

Test If Empty Diagram Window Opens Without Id
    [Documentation]     Checks that empty diagram is successfully opened when the id is nonexisting. Check by user,
    get saved data    asdfg