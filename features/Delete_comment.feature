Feature: Delete a comment
  In order to delete an comment
  As the owner of the comment
  I want to be able to delete my comment instance

  Background:  There are some comments
    Given Exists a user "user1" with password "password"
    And Exists publication registered by "user1"
      | titulo                   |
      | movilidad      |
    And Exists comment at publication "movilidad"
      | Comentario         |
      | bueno              |
      | malo               |

  Scenario:
    Given I login as user "user" with password "password"
    When I try deleting the comment with comment "bueno"
    And There are 1 comment