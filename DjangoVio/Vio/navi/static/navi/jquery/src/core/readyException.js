define( [
	"_jquery@3.4.1@jquery/dist/core"
], function( jQuery ) {

"use strict";

jQuery.readyException = function( error ) {
	window.setTimeout( function() {
		throw error;
	} );
};

} );
