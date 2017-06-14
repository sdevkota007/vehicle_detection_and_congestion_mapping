$('input#name-submit').on('click', function(){
	var Id = $('input#name').val();
	if($.TRIM(Id) != ''){
		$.POST('ajax/ajax.php', {Id: Id}, function(data){
			$('div#name-data').text(data);
		});
	}
});

$('input#name-submit').on('click', function(){
	alert("HAHA")
});