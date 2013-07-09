# Judgmental

Pops up an API and a website for judicial opinions for a given court.

## Use

Provided with a list of PDF-based court opinions, this extracts text from those legal opinions, performs some natural language processing on that text, creates a JSON-based API and bulk downloads of those decisions, indexes them within a search system, and pops up a website to search, browse, and download those decisions.

### Extracting opinion metadata from converted PDFs

In the VA example we tackled for the Judgmental project, some basic metadata was available from the list of opinions on the VA courts website.  In some states, this isn't the case, and any metadata would have to be pulled out of the PDF itself.  With this in mind, we created a basic metadata extractor that allows a user to define regular expressions and extraction functions for different bits of metadata, and then check the results in a split-screen view to see how good the coverage is.

Once a set of PDFs has been converted into HTML, it all happens in `extractor.html`.

#### Converting PDFs to HTML

Step 1 of the extraction is to convert PDFs to a text format that still preserves some of the spacing.  In this case, we used the command line utility pdftohtml:

http://pdftohtml.sourceforge.net/

It does a pretty good job of preserving line breaks and sequencing, which makes for easier extraction from something like a court opinion, that uses spacing to differentiate otherwise similar bits of text.

Running pdftohtml on every pdf results in a matching set of html files.  Those HTML files can be further stripped down by removing everything that isn't within the `<body>` tags using a little shell script (included as `trim_html.sh`):

    #! /bin/bash
	for i in *
	do
		if [[ $i =~ ".html" ]];
		then
			sed -n '/<BODY>/,$p' $i | tail -n +2 | head -n -2 | sed 's/&#160;/ /g' > $i
		fi
	done

Translation: for each .html file, find the first occurrence of the text `<BODY>` and delete the lines before it.  Then delete that line, and also delete the last two lines (a closing `</BODY>` and `</HTML>`).  As an extra helpful step, replace every instance of `&#160;`, the character code for a non-breaking space, with a simple space instead.

#### Extracting metadata

`extractor.html` consists of a split-screen interface that, when a file is selected from the dropdown, shows the PDF version on the left and the HTML version on the right.  The HTML version is run through every metadata extractor defined in the `regexes` variable in the JavaScript at the bottom of the file, and matches are highlighted in different colors.  In this way, you can cycle through lots of documents and look for both false positives and false negatives.

Each extractor is defined as an object in the `regexes` array.  It has three properties:

* `name`: a name for the field you're extracting, like 'opinion_author'
* `expression`: a regular expression to find matches
* `extractor`: a function that will run on the matched text to pull out the exact value.  This is useful for things like cleaning up capitalization before saving the match, or for pulling out a substring from the match that would be a pain to isolate with just a regular expression.  This is also necessary if you want to do something like a lookbehind, which JavaScript doesn't support.  You can use the /g flag to match ALL instances, otherwise it will only match the first instance.

An example:

	{
	      "name": "lower_court",
	      "expression": /from\s+the\s+(circuit\s+)?court\s+([a-z,-]+\s+)+/im,
	      "extractor": function(matches) { 
	            return matches[0].trim().replace(/^from\s+the\s+/i,'').toTitleCase();
	      }
	}

This extracts the name of the lower court that first heard a case before it got to the Virginia Supreme Court.  Opinions typically list the lower court on a single line in phrasing like "From the Circuit Court of the City of Richmond."  This finds the first instance of such phrasing with a regular expression (roughly: "from the circuit court" followed by any combination of letters, spaces, and dashes, with the word "circuit" optional). It then uses the extractor function to trim extra spaces, remove the phrase "From the," and correct the capitalization.  So, passing "FROM THE CIRCUIT COURT OF THE CITY OF RICHMOND" to the extractor function returns the neat and tidy version, "Circuit Court of the City of Richmond."

#### Notes

* This is all very rough, a quick exercise as part of the [the Knight-Mozilla-MIT “Insider/Outsider” Hack Day](https://wiki.mozilla.org/OpenNews/hackdays/insideroutsider#HackDash:_Project_Teams_and_Ideas) on June 22–23, 2013.  With some more polish, it can be a nice simple interface for aggressively testing regular expression matches against an original document (not even necessarily a PDF!).
* If two different extractors will match the same text, this creates problems for the syntax highlighting, because it adds `<span>` tags around matches.  For example, if you have an extractor that matches the name "Richmond" and one that matches the entire phrase "From the Circuit Court of the City of Richmond", you might have a problem.  The first version would replace "Richmond" with something like `<span style="background-color: red;">Richmond</span>` and the second extractor would be matching against that.  Using this seriously would require addressing that overlap problem first.

## Credits

Created by Mariano Blejman, Chase Davis, John Emhoff, Waldo Jaquith, Joanna Kao, Dhanraj Konduru, Matt McDonald, Max Ogden, and Noah Veltman, as part of [the Knight-Mozilla-MIT “Insider/Outsider” Hack Day](https://wiki.mozilla.org/OpenNews/hackdays/insideroutsider#HackDash:_Project_Teams_and_Ideas) on June 22–23, 2013.

## License

Released under the MIT license.
