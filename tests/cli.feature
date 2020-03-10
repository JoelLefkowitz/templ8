Feature: Cli

Scenario Outline: Invalid command handling
    When I call <call>
    Then An InvalidCommand Exception is raised
    And Command issues are reported
    And Correct usage examples are shown
  
    Examples:
        | call                          |
        | templ8                        |
        | templ8 generate extra-command |
        | templ8 --not-an-option        |
        | templ8 --overwrite --dry-run  |
