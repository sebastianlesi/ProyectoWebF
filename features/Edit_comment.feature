Feature: Edit Comment
In order to keep track of the changes I do,
As a user,
I want to edit a comment register I created.

Background: There are registered users and a comment by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists publication registered by "user1"
      | titulo          |
      | The Tavern      |
    And Exists comment at publication "The Tavern" by "user2"
      | comentario      |
      | bueno           |

  Scenario: Edit owned comment registry
    Given I login as user "user2" with password "password"
    When I view the details for comment "bueno"
    And I edit the current dish
      | comentario     |
      | malo           |
    Then I'm viewing the details page for comment at publication "The Tavern" by "user2"
      | comentario     |
      | malo           |
    And There are 1 comments
