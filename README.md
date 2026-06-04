# Family Tree Manager

Python application for managing family relationships with an object-oriented design. Tracks multiple generations, calculates family statistics, and handles complex relationships like divorced parents and extended family.

## Features

- Add people (living or deceased) with biographical data
- Define relationships (parents, children, partners, siblings)
- Query immediate family (parents, children, spouse)
- Query extended family (aunts, uncles, cousins)
- Track birthdays by month
- Calculate statistics (average age at death, average children per person)

## How to Run
```bash
python main.py
```

**Output includes:**
- Full family tree with all 23 members
- Family relationships for specific people
- Birthday list for any month
- Statistical analysis (average age at death, children per person)

## Run Tests
```bash
python test_family_tree.py
```

## Tech Stack

- Python 3.x
- Object-oriented design (classes for Person, DeceasedPerson, Parent, Child)
- Unit tests with unittest module (12 test cases)

## Project Structure
```
Person.py           # Core Person class and subclasses
FamilyTree.py       # FamilyTree manager and BirthdayManager
main.py             # Demo with sample family data (23 people, 3 generations)
test_family_tree.py # Unit tests covering edge cases
```

## What I Learned

- Designing class hierarchies and inheritance in Python
- Managing bidirectional relationships (parent-child, siblings)
- Writing comprehensive unit tests for edge cases
- Handling data validation and error cases
- Working with dates and calculating statistics

## Example Output
```
Family Tree Members: 23 people across 3 generations
Average Age at Death: 70.00 years
Total Children: 10
Average Children per Person: 0.43

Upcoming Birthdays in May:
- Maria (12/05/1970)
- Lucia (18/05/2000)
- Manuel (10/05/1900)
```

## Future Improvements

- Add SQLite database for persistence
- Build CLI interface for interactive data entry
- Generate visual family tree diagram
- Export to GEDCOM format