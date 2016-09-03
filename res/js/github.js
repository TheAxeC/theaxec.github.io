jQuery(document).ready(function() {
	
	$('#gf').text('GitHub Followers');
    $('#gfr').text('GitHub Repos');		

	
	JSONP( 'https://api.github.com/users/theaxec?callback=?', function( response ) {
		var data = response.data;
		if (typeof data.followers !== 'undefined') {
			$('#gf').text(data.followers + ' GitHub Followers');
		}
		if (typeof data.public_repos !== 'undefined') {
        	$('#gfr').text(data.public_repos + ' GitHub Repos');
        }
	});
	
	function JSONP( url, callback ) {
		var id = ( 'jsonp' + Math.random() * new Date() ).replace('.', '');
		var script = document.createElement('script');
		script.src = url.replace( 'callback=?', 'callback=' + id );
		document.body.appendChild( script );
		window[ id ] = function( data ) {
			if (callback) {
				callback( data );
			}
		};
	}	

});