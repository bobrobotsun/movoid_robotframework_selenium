*** Settings ***
Library            RobotFrameworkSelenium
Library            Selenium2Library

*** Keywords ***
suite-setup
    Create Webdriver    Chrome
    Config Init
    Selenium Init

test-setup
    Config Use Suite Case List

test-setup2
    Log    123
    
func1
    [Arguments]    ${param1}
    Log    ${param1}