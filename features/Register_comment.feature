Feature: Register Comment
In order to keep track of the comment I make,
As a user
I want to register a comment in the corresponding publication together with its details.

 Background: There is a registered user and publication
    Given Exists a user "user" with password "password"

  Scenario: Register just comment
    Given I login as user "user" with password "password"
    When I register comment at publication "The Tavern"
      | comentario      |
      | bueno           |
    Then I'm viewing the details page for comment at publication "The Tavern" by "user"
      | comentario      |
      | bueno           |
    And There are 1 comments