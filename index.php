<?php

/*
 * Retrieve the list of all opinions from its JSON file.
 */
$json = file_get_contents('/opinions.json');

if ($json === FALSE)
{
	die('Could not open the list of opinions.');
}

/*
 * Convert the JSON file into a PHP object.
 */
$opinions = json_decode($json);

if ($opinions === FALSE)
{
	die('Opinion JSON is corrupt.');
}

echo '	<table id="resultsTable" class="tablesorter">
		<thead>
			<tr>
				<th>Case</a></th>
				<th>Date</th>
				<th>Summary</th>
			</tr>
		</thead>
		<tbody>';

/*
 * Iterate through the opinions and display each one.
 */
foreach ($opinions as $opinion)
{
	
	/* 
	 * Set aside the words that comprise the first 140 characters of the opinion text.
	 */
	$tmp = wordwrap($opinion->summary, 140, '<!-->')
	$tmp = explode('<!-->', $tmp);
	$opinion->summary = $tmp[0];
	unset($tmp);
	
	echo '	<tr>
				<td><a href="opinion.php?number=' . $opinion->number . ' ">' . $opinion->name . '</a></td>
				<td>' . $opinion->date_published . '</td>
				<td>' . $opinion->summary . '</td>
			</tr>';
	
}

echo '</tbody></table>';