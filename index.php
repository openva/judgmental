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

echo '	<table>
		<thead>
			<tr>
				<th>Case</a></th>
				<th>Date</th>
				<th>Number</th>
			</tr>
		</thead>
		<tbody>';

foreach ($opinions as $opinion)
{
	echo '	<tr>
				<td><a href="opinion.php?number=' . $opinion->number . ' ">' . $opinion->name . '</a></td>
				<td>' . $opinion->date_published . '</td>
				<td>' . $opinion->numer . '</td>
			</tr>';
}

echo '</tbody></table>';