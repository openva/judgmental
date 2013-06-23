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
yes

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
Richmond

### Field Name
court_location

### Data Type
string

### Required
no

### Notes
While this is unstructured text, it ought to be a placename, and may be geocodable.


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
It's not yet clear what this is going to look like. Noah should have some ideas about this.


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
Given the nature of appeals (the role of the parties depends on who appeals, so it can reverse along the way), is there even value in storing whether somebody is the plaintiff or the defendant?


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
We need to store the names of the judges who heard the case, and we need to store the name of the author of the opinions? Should we turn this into an indexed array, in which we identify the judge who is the author? Or should we store the author's identity in a different field? Is it possible for the author of a decision to be somebody other than one of the judges who heard or ruled on the case?


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
Some laws are cited repeatedly. Do we want to store a representation of the unique laws that were cited, or do we want to store a representation of all citations? That is, are we telling people that §&nbsp;38.2-2206 was cited 3 times, or just that it was cited at *all*?


## Cited Cases

### Example
unclear—working on this

### Field Name
cited cases

### Data Type
indexed array

### Required
no

### Notes
Some cases are cited repeatedly. See [Cited Laws](#Cited%20Laws) for the ramifications of this.


## Decision Text

### Example
array(
	'format' => 'pdf', url => 'http://www.courts.state.va.us/opinions/opnscvwp/1981428.pdf',
	'format' => 'txt', url => '/rulings/1981428.txt'
)

### Field Name
text

### Data Type
array

### Required
yes

### Notes
This does not store the actual text, but just a link the text in its various formats.
