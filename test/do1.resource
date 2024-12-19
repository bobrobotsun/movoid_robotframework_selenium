*** Settings ***
Library            RobotFrameworkSelenium
Library            Selenium2Library

*** Keywords ***
suite-setup
    selenium_init
    selenium Create webdriver

suite-teardown
    Selenium Close Webdriver

test-setup
    Print    1

test-setup2
    Print    123
    
func1
    [Arguments]    ${param1}
    Print    ${param1}