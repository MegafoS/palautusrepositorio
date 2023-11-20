*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  galle
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Register With Valid Username And Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  mafia
    Register Password  mafia123
    Register New Account
    Register Should Succeed


Register With Too Short Username And Valid Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  mp
    Set Password  mafia123
    Register New Account
    Register Should Fail With Message  Username must be atleast 3 letters long

Register With Valid Username And Too Short Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  mafia
    Set Password  mafia12
    Register New Account
    Register Should Fail With Message  Password must be atleast 8 letters long

Register With Valid Username And Invalid Password
    Go To Register Page
    Register Page Should Be Open
    Set Username  mafia
    Set Password  mafiayksikaksikolme
    Register New Account
    Register Should Fail With Message  Password must contain weird letters!

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Register Page Should Be Open
    Set Username  mafia
    Set Password  mafia123
    Set Password  mafia456
    Register New Account
    Register Should Fail With Message  Passwords must match

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Register New Account
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
Register Password 
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Go To Register Page For New Account
    Go To Register Page    
