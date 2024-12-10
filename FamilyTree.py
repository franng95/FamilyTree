from Person import Person
from Person import DeceasedPerson
from Person import Parent

class FamilyTree:
    """
    Manages the family tree, providing functionality to add people,
    define relationships, and query the tree.
    """

    # Collaborative Work: This class was primarily developed by Ismael, with Fran contributing to the development of
    # specific methods.
    # Some specific methods (e.g., `get_average_age_at_death`) were particularly challenging
    # due to their statistical logic, for which we sought clarification and guidance from ChatGPT.

    def __init__(self):
        """
        Initializes an empty family tree.
        """
        self.members = {}  # Dictionary to store members by their name

    def add_person(self, person):
        """
        Adds a person to the family tree.

        Args:
            person (Person): The person to add.

        Raises:
            ValueError: If the person is not a Person object or already exists in the tree.
        """
        if not isinstance(person, Person):
            raise ValueError("Only Person objects can be added to the family tree.")
        if person.name in self.members:
            raise ValueError(f"A person named {person.name} already exists in the family tree.")
        self.members[person.name] = person

    def get_person(self, name):
        """
        Retrieves a person from the family tree by name.

        Args:
            name (str): The name of the person to retrieve.

        Returns:
            Person: The person object if found, else None.
        """
        return self.members.get(name)

    def display_tree(self, root_name):
        """
        Displays the family tree starting from a specific person.

        Args:
            root_name (str): The name of the root person.
        """
        root = self.get_person(root_name)
        if not root:
            print(f"No person named {root_name} found in the family tree.")
            return

        print(f"Family Tree of {root_name}:")
        root.display_family_tree()  # Placeholder for a future method in the Person class.

    def list_all_members(self):
        """
        Lists all members of the family tree.
        """
        print("Members of the Family Tree:")
        for name, person in self.members.items():
            print(f"- {name} ({person.gender})")

    def get_average_age_at_death(self):
        """
        Calculates the average age at death for all deceased individuals in the family tree.

        Returns:
            float or None: Average age at death, or None if no deceased individuals exist.

        Note:
            The logic for this method required understanding how to handle missing or improperly formatted
            data while iterating over a large dataset. We referred to ChatGPT to clarify edge cases and
            ensure robustness. Fran has contributed to this method.
        """
        total_age = 0
        count = 0

        for person in self.members.values():
            if isinstance(person, DeceasedPerson):
                age = person.get_age_at_death()
                if age is not None:
                    total_age += age
                    count += 1

        return total_age / count if count > 0 else None

    def get_total_number_of_children(self):
        """
        Calculates the total number of children in the family tree.

        Returns:
            int: Total number of children.
        """

        #Fran has contributed to this method

        total_children = 0
        for person in self.members.values():
            total_children += len(person.children)
        return total_children

    def get_average_number_of_children(self):
        """
        Calculates the average number of children per individual in the family tree.

        Returns:
            float: Average number of children, or None if no members exist.

        Note:
            This method, though simpler, still required clear iteration logic over the members and their children.
            We clarified the statistical approach using ChatGPT when integrating edge cases.
            Fran has contributed to this method.
        """
        total_children = self.get_total_number_of_children()
        total_members = len(self.members)
        return total_children / total_members if total_members > 0 else None

class Child(Person):
    """
    Represents a child in the family tree, extending Person.
    """

    # Developed by Francisco
    # The design of this class was straightforward, focusing on extending functionality for children,
    # such as additional details like grade.

    def __init__(self, name, gender, birth_date=None, grade=None):
        """
        Initializes a child with additional details.

        Args:
            grade (str, optional): The grade level of the child. Defaults to None.
        """
        super().__init__(name, gender, birth_date)
        self.grade = grade  # Specific attribute for Child instances

    def get_child_details(self):
        """
        Returns details about the child.

        Returns:
            str: A formatted string with the child's details.
        """
        details = f"Name: {self.name}, Gender: {self.gender}, Grade: {self.grade}"
        if self.birth_date:
            details += f", Birth Date: {self.birth_date}"
        return details


class BirthdayManager:
    """
    Manages and tracks birthdays in the family tree.
    """

    # Developed by Ismael
    # The logic for this class required sorting and filtering family member data by dates,
    # which was an excellent exercise in parsing and organizing data.

    def __init__(self, family_tree):
        """
        Initializes the BirthdayManager.

        Args:
            family_tree (FamilyTree): The family tree to manage birthdays for.
        """
        self.family_tree = family_tree

    def get_upcoming_birthdays(self, month):
        """
        Retrieves family members with birthdays in a given month.

        Args:
            month (int): The month (1-12) to check for birthdays.

        Returns:
            list[Person]: A list of people with birthdays in the specified month.

        Note:
            The logic for filtering and extracting the correct month from the birth_date attribute
            was discussed with ChatGPT to ensure proper handling of edge cases (e.g., invalid or missing dates).
        """
        upcoming_birthdays = []
        for person in self.family_tree.members.values():
            if person.birth_date:
                birth_month = int(person.birth_date.split("/")[1])  # Extract month from DD/MM/YYYY
                if birth_month == month:
                    upcoming_birthdays.append(person)
        return upcoming_birthdays

    def display_upcoming_birthdays(self, month):
        """
        Displays the names of family members with upcoming birthdays.

        Args:
            month (int): The month (1-12) to check for birthdays.
        """
        people_with_birthdays = self.get_upcoming_birthdays(month)
        if not people_with_birthdays:
            print(f"No birthdays found for month {month}.")
            return

        print(f"Upcoming Birthdays in Month {month}:")
        for person in people_with_birthdays:
            print(f"- {person.name} ({person.birth_date})")
