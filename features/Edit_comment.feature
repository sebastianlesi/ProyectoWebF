Feature: Edit Comment
In order to keep updated my previous registers about comments
As a user,
I want to edit a comment register I created.
Background: There are registered users and a comment by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists publication registered by "user1"
      | titulo                   |
      | Movilidad en España      |
    And Exists comment at publication "Movilidad en España"
      | id_comentario   | comentario      |
      | 0               | bueno           |

  Scenario: Edit owned comment registry
    Given I login as user "user2" with password "password"
    When I edit the comment at publication with the id_comentario "0"
      | id_comentario   | comentario      |
      | 0               | malo           |
    Then There are 1 comments
