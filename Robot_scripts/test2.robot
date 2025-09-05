*** Settings ***
Library    OperatingSystem
*** Keywords ***

*** Variables ***
@{list}    mani    harish    nandagopal
*** Test Cases *** 
TEST2
    [Tags]    P3
    Log    This is sample test case
    Log    ${list}
    Log    The third value of the list is ${list}[2]