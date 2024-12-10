# Francisco has developed this part

class Person:
    """
    Represents an individual in a family tree.
    Provides core functionality to manage personal relationships and details.
    """

    def __init__(self, name, gender, birth_date=None):
        """
        Initializes a Person with basic details.

        Args:
            name (str): Name of the person.
            gender (str): Gender of the person.
            birth_date (str, optional): Birth date in 'YYYY-MM-DD' format. Defaults to None.
        """
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.children = []  # Stores child objects related to this person
        self.partner = None  # Current partner
        self.last_partners = []  # List of past partners for tracking relationships
        self.mum = None  # Reference to mother, if known
        self.dad = None  # Reference to father, if known
        self.siblings = []  # List of sibling objects

    def add_child(self, child):
        """
        Adds a child to the person and links the child to this person as their parent.

        Args:
            child (Person): The child to add.

        Raises:
            ValueError: If the provided child is not a Person object.
        """
        if not isinstance(child, Person):
            raise ValueError("Child must be a Person object.")
        self.children.append(child)
        # Automatically link the parent to the child
        if self.gender == "Male":
            child.dad = self
        elif self.gender == "Female":
            child.mum = self

    def set_partner(self, partner):
        """
        Sets or updates a partner for the person, tracking past partners if applicable.

        Args:
            partner (Person): The partner to set.

        Raises:
            ValueError: If the provided partner is not a Person object.
        """
        if not isinstance(partner, Person):
            raise ValueError("Partner must be a Person object.")

        # Move the current partner to the list of past partners, if any
        if self.partner is not None:
            if self.partner not in self.last_partners:
                self.last_partners.append(self.partner)
            # Break the reciprocal relationship
            if self.partner.partner == self:
                self.partner.partner = None

        self.partner = partner  # Update to the new partner

        # Ensure the relationship is mutual
        if partner.partner != self:
            partner.set_partner(self)

    def add_sibling(self, sibling):
        """
        Adds a sibling to the person and establishes a mutual sibling relationship.

        Args:
            sibling (Person): The sibling to add.

        Raises:
            ValueError: If the provided sibling is not a Person object.
        """
        if not isinstance(sibling, Person):
            raise ValueError("Sibling must be a Person object.")
        if sibling not in self.siblings:
            self.siblings.append(sibling)
            sibling.siblings.append(self)

    def get_past_partners(self):
        """
        Retrieves the names of past partners.

        Returns:
            list[str]: Names of all past partners.
        """
        return [partner.name for partner in self.last_partners]

    def get_full_details(self):
        """
        Provides a formatted string summarizing the person's details.

        Returns:
            str: A summary including name, gender, partner, children, parents, and siblings.
        """
        details = f"Name: {self.name}, Gender: {self.gender}"
        if self.partner:
            details += f", Partner: {self.partner.name}"
        else:
            if self.last_partners:
                past_partner_names = ", ".join(self.get_past_partners())
                details += f", Currently single. Previously with: {past_partner_names}"
            else:
                details += ", Currently single with no past partners"
        if self.children:
            child_names = ", ".join(child.name for child in self.children)
            details += f", Children: {child_names}"
        if self.mum or self.dad:
            parents = []
            if self.mum:
                parents.append(f"Mother: {self.mum.name}")
            if self.dad:
                parents.append(f"Father: {self.dad.name}")
            details += f", Parents: {', '.join(parents)}"
        if self.siblings:
            sibling_names = ", ".join(sibling.name for sibling in self.siblings)
            details += f", Siblings: {sibling_names}"
        return details

    def get_immediate_family(self):
        """
        Retrieves immediate family members.

        Returns:
            dict: Immediate family categorized into parents, siblings, spouse, and children.
        """
        immediate_family = {
            "parents": [],
            "siblings": [],
            "spouse": None,
            "children": []
        }

        if self.mum:
            immediate_family["parents"].append(self.mum.name)
        if self.dad:
            immediate_family["parents"].append(self.dad.name)

        immediate_family["siblings"] = [sibling.name for sibling in self.siblings]

        if self.partner:
            immediate_family["spouse"] = self.partner.name

        immediate_family["children"] = [child.name for child in self.children]

        return immediate_family

    def get_extended_family(self):
        """
        Retrieves extended family members such as aunts, uncles, and cousins.

        Returns:
            dict: Extended family categorized into aunts, uncles, and cousins.

        Note:
            The logic for recursively exploring relationships (e.g., cousins and aunts/uncles)
            was particularly challenging. We sought guidance from ChatGPT to clarify the
            relationship traversal and ensure consistency, as this is a complex aspect for beginners.
        """
        extended_family = {
            "aunts": [],
            "uncles": [],
            "cousins": []
        }

        if self.mum:
            for sibling in self.mum.siblings:
                if sibling.gender == "Female":
                    extended_family["aunts"].append(sibling.name)
                elif sibling.gender == "Male":
                    extended_family["uncles"].append(sibling.name)
                extended_family["cousins"] += [child.name for child in sibling.children]

        if self.dad:
            for sibling in self.dad.siblings:
                if sibling.gender == "Female":
                    extended_family["aunts"].append(sibling.name)
                elif sibling.gender == "Male":
                    extended_family["uncles"].append(sibling.name)
                extended_family["cousins"] += [child.name for child in sibling.children]

        return extended_family


class Parent(Person):
    """
    Represents a parent in the family tree, extending the Person class.
    """

    def get_number_of_children(self):
        """
        Retrieves the total number of children.

        Returns:
            int: Total number of children.
        """
        return len(self.children)

    def get_child_names(self):
        """
        Retrieves the names of all children.

        Returns:
            list[str]: Names of the children.
        """
        return [child.name for child in self.children]


class DeceasedPerson(Person):
    """
    Represents a deceased person in the family tree, extending the Person class.
    """

    def __init__(self, name, gender, birth_date=None, death_date=None):
        """
        Initializes a DeceasedPerson with death-related details.

        Args:
            death_date (str, optional): Date of death in 'DD/MM/YYYY' format.

        Note:
            We consulted ChatGPT for assistance in implementing the parsing of birth
            and death dates to calculate age at death, as handling these string operations
            and edge cases was particularly complex for a first-term project.
        """
        super().__init__(name, gender, birth_date)
        self.death_date = death_date

    def get_age_at_death(self):
        """
        Calculates the age at the time of death.

        Returns:
            int or None: Age at death if dates are valid, otherwise None.
        """
        if self.birth_date and self.death_date:
            try:
                birth_parts = self.birth_date.split("/")
                death_parts = self.death_date.split("/")
                if len(birth_parts) == 3 and len(death_parts) == 3:
                    return int(death_parts[2]) - int(birth_parts[2])
            except (ValueError, IndexError):
                return None
        return None
