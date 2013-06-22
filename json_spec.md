# JSON File Specification

A description of the fields within the JSON file for each case.


## Case Name

### Example

### Field Name
`name`

### Data Type
string

### Required
yes

## Case Number
`number`

### Example

### Field Name

### Data Type
string

### Required

### Notes


## Date Published
`published`

### Example

### Field Name

### Data Type
date

### Required
yes

### Notes


## Court Name

### Example

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

### Field Name
outcome

### Data Type
unknown

### Required
no

### Notes


## Parties

### Example

### Field Name
parties

### Data Type
array

### Required
yes

### Notes


## Judges

### Example

### Field Name
judges

### Data Type
array

### Required
no

### Notes


## Attorneys

### Example

### Field Name
attorneys

### Data Type
array

### Required
no

### Notes


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
