*** Settings ***
Library            RobotFrameworkSelenium
Library            Selenium2Library

*** Keywords ***
suite-setup
    Create Webdriver    Chrome
    Selenium Init

test-setup
    Print    1

test-setup2
    Print    123
    
func1
    [Arguments]    ${param1}
    Print    ${param1}