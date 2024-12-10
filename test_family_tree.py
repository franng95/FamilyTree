import unittest
from Person import Person, DeceasedPerson
from FamilyTree import FamilyTree


class TestFamilyTree(unittest.TestCase):
    """
    Unit tests for the FamilyTree application to ensure functionality
    and robustness of the implemented features.
    """

    def setUp(self):
        """
        Set up a basic family tree structure for testing purposes.
        This includes creating initial members and adding relationships.

        Note:
        The overall structure and logic were designed by us, but assistance was
        sought from ChatGPT for ideas on ensuring efficient setup for multiple test cases.
        """
        self.family_tree = FamilyTree()

        # Adding initial test members
        self.john = Person(name="John", gender="Male", birth_date="1980-05-10")
        self.jane = Person(name="Jane", gender="Female", birth_date="1982-08-25")
        self.lucas = Person(name="Lucas", gender="Male", birth_date="2005-03-30")
        self.emma = Person(name="Emma", gender="Female", birth_date="2008-11-12")

        # Establishing relationships
        self.john.add_child(self.lucas)
        self.john.add_child(self.emma)

        # Adding members to the family tree
        self.family_tree.add_person(self.john)
        self.family_tree.add_person(self.jane)
        self.family_tree.add_person(self.lucas)
        self.family_tree.add_person(self.emma)

    def test_immediate_family(self):
        """
        Test to verify the retrieval of an individual's immediate family,
        including children, spouse, and parents.

        Note:
        We designed this test, but ChatGPT assisted in clarifying the expected outputs
        for specific edge cases, such as individuals with no defined family relationships.
        """
        immediate_family = self.john.get_immediate_family()
        self.assertEqual(immediate_family["children"], ["Lucas", "Emma"])

    def test_extended_family(self):
        """
        Test to verify the retrieval of an individual's extended family,
        including aunts, uncles, and cousins.
        """
        extended_family = self.lucas.get_extended_family()
        self.assertEqual(extended_family["aunts"], [])
        self.assertEqual(extended_family["cousins"], [])

    def test_average_age_at_death(self):
        """
        Test to calculate the average age at death for deceased individuals
        in the family tree.

        Note:
        Assistance was sought from ChatGPT for ideas on how to handle edge cases
        like missing or invalid dates.
        """
        deceased_person = DeceasedPerson(name="Paul", gender="Male", birth_date="01/01/1950", death_date="01/01/2000")
        self.family_tree.add_person(deceased_person)
        avg_age = self.family_tree.get_average_age_at_death()
        self.assertEqual(avg_age, 50)  # Expecting the average age to be 50

    def test_total_and_average_children(self):
        """
        Test to calculate the total and average number of children
        across all members in the family tree.
        """
        total_children = self.family_tree.get_total_number_of_children()
        average_children = self.family_tree.get_average_number_of_children()
        self.assertEqual(total_children, 2)
        self.assertAlmostEqual(average_children, 0.5)

    def test_person_with_no_relations(self):
        """
        Test for individuals with no defined relationships in the family tree.
        Ensures the program handles such cases gracefully.
        """
        orphan = Person(name="Orphan", gender="Female")
        self.family_tree.add_person(orphan)
        immediate_family = orphan.get_immediate_family()
        extended_family = orphan.get_extended_family()
        self.assertEqual(immediate_family["parents"], [])
        self.assertEqual(immediate_family["children"], [])
        self.assertEqual(extended_family["aunts"], [])
        self.assertEqual(extended_family["cousins"], [])

    def test_past_partners(self):
        """
        Test to verify the handling of past partners when setting a new partner
        for an individual.

        Note:
        The logic for updating past partners was challenging to design, so we
        sought guidance from ChatGPT for edge cases, such as removing reciprocal
        relationships.
        """
        self.john.set_partner(self.jane)
        new_partner = Person(name="Clara", gender="Female")
        self.family_tree.add_person(new_partner)
        self.john.set_partner(new_partner)
        self.assertIn("Jane", self.john.get_past_partners())
        self.assertEqual(self.john.partner.name, "Clara")

    def test_maternal_paternal_branches(self):
        """
        Test to ensure integration of maternal and paternal branches
        in the family tree.
        """
        maternal_grandparent = Person(name="Margaret", gender="Female")
        paternal_grandparent = Person(name="George", gender="Male")
        self.family_tree.add_person(maternal_grandparent)
        self.family_tree.add_person(paternal_grandparent)
        self.assertIn("Margaret", [p.name for p in self.family_tree.members.values()])
        self.assertIn("George", [p.name for p in self.family_tree.members.values()])

    def test_large_family_tree(self):
        """
        Performance test to verify handling of a large family tree
        with thousands of members.

        Note:
        ChatGPT provided advice on how to structure this test to ensure efficient
        addition and counting of large datasets.
        """
        for i in range(1000):
            person = Person(name=f"Person_{i}", gender="Male")
            self.family_tree.add_person(person)
        self.assertEqual(len(self.family_tree.members), 1004)  # Includes initial 4 members

    def test_invalid_person(self):
        """
        Test to verify error handling when attempting to add
        invalid data to the family tree.
        """
        with self.assertRaises(ValueError):
            self.family_tree.add_person("NotAPerson")

    def test_missing_birth_date(self):
        """
        Test to verify handling of individuals with no birth date specified.
        """
        person = Person(name="Alex", gender="Male")
        self.family_tree.add_person(person)
        self.assertEqual(person.birth_date, None)

    def test_empty_family_tree(self):
        """
        Test to ensure proper initialization of an empty family tree.
        """
        empty_tree = FamilyTree()
        self.assertEqual(len(empty_tree.members), 0)

    def test_large_family_tree(self):
        """
        Performance test for a very large family tree with over 10,000 members.

        Note:
        ChatGPT clarified the best practices for structuring a performance test
        and ensuring edge cases (e.g., very large data handling) were accounted for.
        """
        for i in range(10000):
            self.family_tree.add_person(Person(name=f"Person_{i}", gender="Male"))
        self.assertEqual(len(self.family_tree.members), 10000 + 4)  # Includes the 4 initial members


if __name__ == "__main__":
    unittest.main()
