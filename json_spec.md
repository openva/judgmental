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

### Notes


## Court Name

### Example

### Field Name
court

### Data Type
string

### Required

### Notes


## Court Location

### Example

### Field Name
court_location

### Data Type
string

### Required

### Notes


## Outcome

### Example

### Field Name
outcome

### Data Type
unknown

### Required

### Notes


## Parties

### Example

### Field Name
parties

### Data Type
array

### Required

### Notes


## Judges

### Example

### Field Name
judges

### Data Type
array

### Required

### Notes


## Attorneys

### Example

### Field Name
attorneys

### Data Type
array

### Required

### Notes


## Type of Case

### Example
civil

### Field Name
type

### Data Type
enum: `civil` or `criminal`

### Required

### Notes


## Cited Laws

### Example

### Field Name
cited laws

### Data Type
{ citation # }

### Required

### Notes


## Cited Cases

### Example

### Field Name
cited cases

### Data Type
{ case # }

### Required

### Notes


## Decision Text

### Example

### Field Name
text

### Data Type
array { format, URL }

### Required

### Notes
