*** Settings ***
Resource          do1.resource

*** Test Cases ***
01_do1
    Go To    http://www.baidu.com
    Robot Check Param    467    str
    Robot Check Param    1    int
    Robot Check Param    1   float
    Robot Check Param    true    bool
    Robot Check Param    false    bool
    Robot Check Param    ${EMPTY}    bool
    Robot Check Param    [1,2,3]    list
    Robot Check Param    {1:1,2:2}    dict
    test123
    Selenium Log Screenshot
    selenium_get_element_color_list
    Selenium Html Wait Until Find Element    //div

#    Log    ${_config}[a]
#    Func1    ${_config}[a]

#02_do2
#    Log    ${_config}[a]
#    Func1    ${_config}[a]
