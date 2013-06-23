$(document).ready(function(){
	$("#resultsTable").tablesorter({sortList: [[0,0]]});
	$("#category").dropdownchecklist({firstItemChecksAll: 'exclusive' });
	$("#category").css({'visibility': 'visible'});

	$('#searchbutton').click(function() {
		var keyword, category;
		
		keyword = $('#keyword').val();
		category = $.map($('#category option:selected'), function(selected) { return selected.value; });

		$('#resultsTable tbody tr').remove();

		displayData(keyword, category);
	});

	function displayData(keyword, category) {
		var content;
		$.ajax({ // use search api and return document numbers
			url: 'http://yqoffbyc.api.qbox.io/opinions/_search?q='+encodeURIComponent(escape(keyword)),
		}).done(function(searchresults) {
			console.log(searchresults);
			$.each(searchresults.hits.hits, function(searchindex, searchvalue) {
				// console.log(searchvalue);
				var opinionid = searchvalue._source.number;
				$.ajax({
					url: 'opinions/'+opinionid+'.json',
				}).done(function(data) {
					$.each(data.hits.hits, function(index, value) {
						content = $('<tr>'+
			                			'<td><a href="opinion.php?number=' + value.number + ' ">' + value.name + '</a></td>'+
										'<td>' + value.date_published + '</td>'+
										'<td>' + value.summary + '</td>'+
			            			'</tr>');
					    $('#resultsTable tbody').append(content);
					    $('#resultsTable').trigger("update")
					});
				});
			});
			// $.ajax({ // loop through each document number and call json
			// 	url: 'opinions/'+id+'.json',
			// }).done(function(data) {
			// 	console.log(data);
			// 	$.each(data.hits.hits, function(index, value) {
			// 		content = $('<tr>'+
		 //                			'<td><a href="opinion.php?number=' + value.number + ' ">' + value.name + '</a></td>'+
			// 						'<td>' + value.date_published + '</td>'+
			// 						'<td>' + value.summary + '</td>'+
		 //            			'</tr>');
			// 	    $('#resultsTable tbody').append(content);
			// 	    $('#resultsTable').trigger("update")
			// 	});
			// });
		});
	}
});

$(document).ajaxStop(function(){
    $("#resultsTable").tablesorter({sortList: [[0,0]]});
});