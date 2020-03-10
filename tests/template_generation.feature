Feature: Template generation

Scenario: Invalid configuration file path
    When I give an invalid configuration file path
    Then A ConfigPathInvalid Exception is raised

Scenario: Spec handling
    Given A spec is set to True in the configuration file
    When I call "templ8 config-file output-dir"
    Then The spec name is set to True in the resolver context
    And The specs context are included in the resolver context

Scenario: Missing configuration
    Given A spec is set to True in the configuration file
    And Context is missing without defualt values 
    When I call "templ8 <config-file> <output-dir>" 
    Then A MissingConfig Exception is raised
    And Missing configuration names are reported

Scenario: Invalid output directory
    When I give an invalid output directory
    Then An OutputDirInvalid Exception is raised

Scenario: Alias handling
    Given A spec is set to True in the configuration file
    And The spec declares an alias
    When I call "templ8 config-file output-dir"
    Then The alias is resolved and included in the resolver context

Scenario: Folder renaming
    Given A spec is set to True in the configuration file
    And The spec declares a folder to rename
    When I call "templ8 config-file output-dir"
    Then The folder to rename is included in the resolver renames, resolving aliases

Scenario: Callback handling
    Given A spec is set to True in the configuration file
    And The spec declares a callback
    When I call "templ8 config-file output-dir"
    Then The callback is included in the resolver callbacks, resolving aliases

Scenario: Output resolver
    When I call "templ8 <config-file> <output-dir>"
    Then Templates are generated in the output directory
    And The resolver context is resolved
    And The resolver renames are resolved
    And The resolver callbacks are called
    And The files generated are reported

Scenario: Output files already exist
    Given Files already exists in the output paths
    When I call "templ8 <config-file> <output-dir>"
    Then Clashing templates are not generated
    And The files skipped are reported
