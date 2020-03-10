Feature: Configuration file generation

Scenario: Configuration file is generated
    When I call "templ8 generate" 
    Then A sequence of interactive text questions are offered
    And A configuration file is generated
