Feature: Register Functionality
  As a new user
  I want to register
  So that I can access my account

  Scenario Outline: Valid register
    Given user in register page
    When user enter fname "<fname>" and mname "<mname>" and lname "<lname>" and password "<password>" and conpass "<conpass>"
    And click register button
    Then register successfully

    Examples:
      | fname | mname | lname | password   | conpass    |
      | ali   | amr   | adel  | hyhy142536 | hyhy142536 |