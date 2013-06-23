<?php

$opinion_number = filter_input(INPUT_GET, 'number', FILTER_SANITIZE_SPECIAL_CHARS);

if (!isset($opinion_number))
{
	die('No opinion number was included in the URL.');
}

/*
 * Retrieve the requested opinion from its JSON file.
 */
$json = file_get_contents('opinions/' . $opinion_number . '.json');

if ($json === FALSE)
{
	die('Could not retrieve opinion ' . $opinion_number);
}

/*
 * Convert the JSON file into a PHP object.
 */
$opinion = json_decode($json);

if ($opinion === FALSE)
{
	die('Opinion JSON is corrupt.');
}

/*
 * Gather the text of the ruling and include that in our object.
 */
$opinion->text->contents = file_get_contents($opinion->text);

echo '<h1>' . $opinion->name . '</h1>';
echo '<h2>' . date('F j, Y', strtotime($opinion->date_published)) . ', Case Number ' . $opinion->number . '</h2>';
echo '<h2>' . $opinion->court . '</h2>';

echo '<dl>';

if (isset($opinion->location))
{
	echo '	<dt>Location</dt>
			<dd>' . $opinion->location . '</dt>';
}

if (isset($opinion->author))
{
	echo '	<dt>Author</dt>
			<dd>' . $opinion->author . '</dt>';
}

if (isset($opinion->outcome))
{
	echo '	<dt>Outcome</dt>
			<dd>' . $opinion->outcome . '</dt>';
}

if (isset($opinion->parties))
{
	echo '	<dt>Plaintiff</dt>
			<dd>' . $opinion->plaintiff . '</dt>
			<dt>Defendant</dt>
			<dd>' . $opinion->defendant . '</dt>';
}

if (isset($opinion->attorneys))
{
	echo '	<dt>Plaintiff’s Attorney</dt>
			<dd>' . $opinion->attorneys->plaintiff . '</dt>
			<dt>Defendant’s Attorney</dt>
			<dd>' . $opinion->attorneys->plaintiff . '</dt>';
}

if (isset($opinion->judges))
{
	echo '	<dt>Judge';
	if (count((array) $opinion->judges) > 1)
	{
		echo 's';
	}
	echo '</dt>
			<dd>'
			. implode($opinion->judges, ', ')
			. '</dt>';
}

if (isset($opinion->cited_laws))
{
	echo '	<dt>Cited Laws</dt>
			<dd>' .
			implode($opinion->cited_laws, ', §&nbsp;') .
			'</dt>';
}

if (isset($opinion->cited_cases))
{
	echo '	<dt>Cited Cases</dt>
			<dd>' .
			implode($opinion->cited_cases, '; ') .
			'</dt>';
}

echo '</dl>';

