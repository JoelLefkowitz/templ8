Feature: Template generation options

Scenario: Generate specific files only
    Given Filenames are specified 
    When I call "templ8 config-file output-dir --overwrite"
    Then Only matching templates are generated in the output directory

Scenario: Skip callbacks when files skipped 
    Given Filenames are specified 
    And Not all of a specs files are specified
    When I call "templ8 config-file output-dir --overwrite"
    Then The resolver callbacks are not called
    And The callbacks that would have been called are reported
    
Scenario: Overwrite files
    Given Files already exists in the output paths
    When I call "templ8 config-file output-dir --overwrite"
    Then Clashing files are overwritten
    And The files overwritten are reported

Scenario: Dont generate files for a dry run
    When I call "templ8 config-file output-dir --dry-run"
    Then All files are skipped
    And The files that would have been generated are reported
    And The files that would not have been generated are reported

Scenario: Dont run callbacks when deactivated 
    When I call "templ8 config-file output-dir --no-callbacks"
    Then The resolver callbacks are not called
    And The callbacks that would have been called are reported
