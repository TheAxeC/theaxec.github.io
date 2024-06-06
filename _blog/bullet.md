---
layout: post
title:  "Bullet Journaling"
picture: /assets/images/projects/default.webp
category: research
publish: False
---

# Bullet Journal

## How to Use It

Bullet journaling is a method of organizing tasks, events, and notes in a single notebook using a specific system of symbols and structures. Here's a simple breakdown. In summary, bullet journaling is a flexible and customizable way to keep track of your life, using simple symbols and logs to organize tasks, events, and notes in a clear and structured manner.

1. **Index**: Start by creating an index to keep track of where each section is in your journal.
2. **Future Log**: List out future events and tasks that aren't tied to a specific month.
3. **Monthly Log**: For each month, create a calendar section for events and a task section for things you want to accomplish.
4. **Daily Log**: Each day, list your tasks, events, and notes. Use symbols to categorize them:
   - Events: `- (o)`
   - Notes: `- (-)` (?, !)
   - Tasks: `- [ ]`
   - Completed Tasks: `- [x]`
   - Migrated Tasks: `- [>]`
   - Migrated Tasks: `- [<]`
   
5. **Collections**: Group related information into collections, like books to read or project plans.

## Code example
```markdown
# Journal
## Index
1. [Future Log](#future-log)
2. [Monthly Log](#monthly-log)
   - [January 2024](#january-2024)
3. [Daily Log](#daily-log)

## Future Log
### 2024
- **January**: 
  - New Year's Eve Party
- **February**: 
  - [ ] Vacation

## Monthly Log
### January 2024

#### Calendar
- 01/01: New Year's Day
- 01/15: Doctor's Appointment

#### Tasks
- [ ] Buy groceries
- [ ] Finish reading book
- [ ] Start exercise routine

## Daily Log
### January 1, 2024
  - (o) New Year's Day lunch with family
  - [ ] Buy groceries
  - [ ] Call John
  - (x) Write journal entry
  - (-) Remember to check the mail

### January 2, 2024
  - (o) Dentist appointment at 3 PM
  - [ ] Clean the house
  - [ ] Finish work project
  - (-) Pick up prescription from pharmacy
```

## YAML Code Example
```yaml
future-log:
  2024:
    january:
      - ["o", "New Year's Eve Party"]
      - ["[ ]", "Vacation"]
monthly-log:
  january-2024:
    calendar:
      - ["01/01", "* o", "New Year's Day"]
      - ["01/15", "o", "Doctor's Appointment"]
    tasks:
      - ["! [ ]", "Buy groceries"]
      - ["[x]", "Call John"]
      - ["[>]", "Finish work project"]
      - ["[<]", "Clean the house"]
daily-log:
  - date: January 1, 2024
    items:
      - ["o", "New Year's Day lunch with family"]
      - ["[ ]", "Buy groceries"]
      - ["[ ]", "Call John"]
  - date: January 2, 2024
    items:
      - ["o", "Doctor's appointment at 3 PM"]
      - ["[ ]", "Clean the house"]
      - ["[ ]", "Finish work project"]
```