Feature: Delete Comment
In order to delete old or useless comment,
As a user,
I want to delete a comment register I created.

Background: There are registered users and a comment by one of them
    Given Exists a user "user" with password "password"
    And Exists a user "user2" with password "password"
    And Exists publication registered by "user1"
      | name            |
      | The Tavern      |
    And Exists comment at publication "The Tavern" by "user2"
      | comentario     |
      | malo           |

  Scenario: Delete owned comment registry
    Given I login as user "user2" with password "password"
    When I view the details for comment "malo"
    And I delete the current dish
      | comentario     |
      |                |
    Then I'm viewing the details page for comment at publication "The Tavern" by "user2"
      | comentario     |
      |                |
    And There are 0 comments