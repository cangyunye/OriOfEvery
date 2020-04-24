define( [
	"_jquery@3.4.1@jquery/src/css/var/cssExpand"
], function( cssExpand ) {
	"use strict";

	return new RegExp( cssExpand.join( "|" ), "i" );
} );
