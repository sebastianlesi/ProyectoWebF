Feature: Delete a publication
  In order to delete an publication
  As the owner of the publication
  I want to be able to delete my publication instance

  Background:  There are some publications
    Given Exists publication registered by "user"
      | titulo         | descripcion | Vistas       |
      | España         | bueno       | 10           |
      | Italia         | malo        | 2            |

  Scenario:
    Given I login as user "user" with password "password"
    When I try deleting the publication with title "Italia"
    And There are 1 publications