define( [
	"_jquery@3.4.1@jquery/src/var/pnum"
], function( pnum ) {

"use strict";

return new RegExp( "^(?:([+-])=|)(" + pnum + ")([a-z%]*)$", "i" );

} );
