*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  galle  galle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  galle123
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input Credentials  g  galle123
    Output Should Contain  Username must be atleast 3 letters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  gg-  galle123
    Output Should Contain  Username cannot be weird letters!

Register With Valid Username And Too Short Password
    Input Credentials  gale  gale123
    Output Should Contain  Password must be atleast 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  gale  galeykskakskolme
    Output Should Contain  Password must contain weird letters!

    
    
*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command
