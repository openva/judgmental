# JSON File Specification

A description of the fields within the JSON file for each case.


## Case Name

### Example
Saint Paul Holmes v. John Doe

### Field Name
name

### Data Type
string

### Required
yes

### Notes
This will generally just be the names of the two parties, but not always.


## Case Number

### Example
981428

### Field Name
number

### Data Type
string

### Required

### Notes
The format of this varies enormously between courts.


## Date Published

### Example
1999-04-16

### Field Name
published

### Data Type
date

### Required
yes

### Notes
Sometimes there are multiple dates, such as when a case is revised. Noah is evaluating. Other fields include the date that the decision was published in a law journal (with no other date provided), the date that a decision was revised, 


## Court Name

### Example
Supreme Court of Virginia

### Field Name
court

### Data Type
string

### Required
yes

### Notes


## Court Location

### Example

### Field Name
court_location

### Data Type
string

### Required
no

### Notes


## Outcome

### Example
Affirmed

### Field Name
outcome

### Data Type
unknown

### Required
no

### Notes


## Parties

### Example
array("plaintiff" => "Saint Paul Holmes", "defendant" => "John Doe")

### Field Name
parties

### Data Type
indexed array

### Required
yes

### Notes


## Judges

### Example
array("Charles L. McCormick, III")

### Field Name
judges

### Data Type
array

### Required
no

### Notes


## Attorneys

### Example
array("plaintiff" => "Lionel Hutz, Esq.", "defendant" => "Miguel Sanchez")

### Field Name
attorneys

### Data Type
indexed array

### Required
no

### Notes
Noah is evaluating the viability of IDing the party whom each attorney represents.


## Type of Case

### Example
civil

### Field Name
type

### Data Type
enum: `civil` or `criminal`

### Required
yes

### Notes


## Cited Laws

### Example
array("38.2-2206", "46.2-1043", "8.01-401.3")

### Field Name
cited laws

### Data Type
{ citation # }

### Required
no

### Notes


## Cited Cases

### Example

### Field Name
cited cases

### Data Type
{ case # }

### Required
no

### Notes


## Decision Text

### Example

### Field Name
text

### Data Type
array { format, URL }

### Required
yes

### Notes
