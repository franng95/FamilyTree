from Person import Person, DeceasedPerson
from FamilyTree import FamilyTree, BirthdayManager

# Initialize the family tree object to store and manage all family members
# This part was implemented by Fran
family_tree = FamilyTree()

# Maternal Branch (María's side)
# This section, including the creation of María's family branch and relationships, was implemented by Fran.
# Some logic for dynamic sibling and child relationships was reviewed with ChatGPT when refining edge cases.
maria = Person(name="María", gender="Female", birth_date="12/05/1970")
ana = DeceasedPerson(name="Ana", gender="Female", birth_date="10/03/1940", death_date="15/06/2000")
juan = DeceasedPerson(name="Juan", gender="Male", birth_date="25/08/1935", death_date="20/11/1995")
laura = Person(name="Laura", gender="Female", birth_date="08/07/1975")
carlos = Person(name="Carlos", gender="Male", birth_date="18/02/1978")
sofia = Person(name="Sofía", gender="Female", birth_date="20/10/1945")
luis = Person(name="Luis", gender="Male", birth_date="15/03/1948")
lucia = Person(name="Lucía", gender="Female", birth_date="18/05/2000")
miguel = Person(name="Miguel", gender="Male", birth_date="12/08/1998")
pablo = Person(name="Pablo", gender="Male", birth_date="30/11/2002")

# Adding maternal family members to the family tree
family_tree.add_person(maria)
family_tree.add_person(ana)
family_tree.add_person(juan)
family_tree.add_person(laura)
family_tree.add_person(carlos)
family_tree.add_person(sofia)
family_tree.add_person(luis)
family_tree.add_person(lucia)
family_tree.add_person(miguel)
family_tree.add_person(pablo)

# Establishing relationships for María's side
# Assistance from ChatGPT: Logic for sibling and parent-child relationships was refined after seeking help.
maria.add_sibling(laura)  # Laura is María's sister
maria.add_sibling(carlos)  # Carlos is María's brother
laura.add_child(lucia)  # Laura's child is Lucía
carlos.add_child(miguel)  # Carlos' child is Miguel
carlos.add_child(pablo)  # Carlos' child is Pablo

# Paternal Branch (Pedro's side)
# This section, including the creation of Pedro's family branch and relationships, was implemented by Ismael.
pedro = Person(name="Pedro", gender="Male", birth_date="18/02/1968")
isabel = Person(name="Isabel", gender="Female", birth_date="12/12/1938")
antonio = DeceasedPerson(name="Antonio", gender="Male", birth_date="15/07/1936", death_date="05/03/1998")
alberto = Person(name="Alberto", gender="Male", birth_date="05/01/1973")
elena = Person(name="Elena", gender="Female", birth_date="22/04/1976")
manuel = DeceasedPerson(name="Manuel", gender="Male", birth_date="10/05/1900", death_date="30/06/1985")
carmen = DeceasedPerson(name="Carmen", gender="Female", birth_date="15/08/1905", death_date="10/09/1988")
clara = Person(name="Clara", gender="Female", birth_date="20/03/1940")
javier = Person(name="Javier", gender="Male", birth_date="10/06/1942")
raquel = Person(name="Raquel", gender="Female", birth_date="05/09/1990")

# Adding paternal family members to the family tree
family_tree.add_person(pedro)
family_tree.add_person(isabel)
family_tree.add_person(antonio)
family_tree.add_person(alberto)
family_tree.add_person(elena)
family_tree.add_person(manuel)
family_tree.add_person(carmen)
family_tree.add_person(clara)
family_tree.add_person(javier)
family_tree.add_person(raquel)

# Establishing relationships for Pedro's side
# Ismael implemented this section, applying similar methods as in María's branch.
pedro.add_sibling(alberto)  # Alberto is Pedro's brother
pedro.add_sibling(elena)  # Elena is Pedro's sister
elena.add_child(raquel)  # Elena's child is Raquel

# Establishing relationships between María and Pedro
# Collaborative effort with guidance from ChatGPT for ensuring proper linking of family relationships.
maria.set_partner(pedro)

# Adding their children
john = Person(name="Juanito", gender="Male", birth_date="10/04/1990")
anita = Person(name="Anita", gender="Female", birth_date="20/09/1992")
marcos = Person(name="Marcos", gender="Male", birth_date="25/01/1994")

maria.add_child(john)
maria.add_child(anita)
maria.add_child(marcos)

pedro.add_child(john)
pedro.add_child(anita)
pedro.add_child(marcos)

# Adding their children to the family tree
family_tree.add_person(john)
family_tree.add_person(anita)
family_tree.add_person(marcos)

# Establishing sibling relationships among María and Pedro's children
# Assistance from ChatGPT: Logic for bidirectional sibling relationships clarified and applied here.
john.add_sibling(anita)
john.add_sibling(marcos)
anita.add_sibling(john)
anita.add_sibling(marcos)
marcos.add_sibling(john)
marcos.add_sibling(anita)

# Display the list of family tree members
# Collaborative section
print("\nFamily Tree Members:")
family_tree.list_all_members()

# Feature 1a: Retrieve parents and grandparents
# Implemented by Fran, logic reviewed with ChatGPT for handling missing grandparents gracefully.
print("\nParents and Grandparents of Juanito:")
print(f"Parents: {john.get_immediate_family()['parents']}")
if maria.mum and maria.dad:
    print(f"Maternal Grandparents: {maria.mum.name}, {maria.dad.name}")
if pedro.mum and pedro.dad:
    print(f"Paternal Grandparents: {pedro.mum.name}, {pedro.dad.name}")

# Feature 1b: Retrieve immediate and extended family
# Implemented by Fran
print("\nImmediate Family of Anita:")
print(anita.get_immediate_family())
print("\nExtended Family of Lucía:")
print(lucia.get_extended_family())

# Feature 2a: Retrieve siblings and cousins
# Implemented by Ismael
print("\nSiblings of Marcos:")
print(marcos.get_immediate_family()["siblings"])
print("\nCousins of Pablo:")
pablo_extended_family = pablo.get_extended_family()
print(f"Cousins: {pablo_extended_family['cousins']}")

# Feature 2b: Manage birthdays
# Implemented by Ismael
birthday_manager = BirthdayManager(family_tree)
print("\nUpcoming Birthdays in Month 5:")
birthday_manager.display_upcoming_birthdays(5)

# Feature 3a: Calculate average age at death
# Collaborative section
avg_age_at_death = family_tree.get_average_age_at_death()
if avg_age_at_death is not None:
    print(f"\nAverage Age at Death: {avg_age_at_death:.2f} years")
else:
    print("\nNo deceased individuals to calculate average age at death.")

# Feature 3b: Calculate total and average number of children
# Collaborative section
total_children = family_tree.get_total_number_of_children()
average_children = family_tree.get_average_number_of_children()
print(f"\nTotal Number of Children: {total_children}")
print(f"Average Number of Children per Person: {average_children:.2f}")

# Feature 3b.i: Number of Children for Each Individual
print("\nNumber of Children for Each Individual:")
for person_name, person in family_tree.members.items():
    number_of_children = len(person.children)
    print(f"{person_name}: {number_of_children} children")
