define( [
	"_jquery@3.4.1@jquery/src/var/support"
], function( support ) {

"use strict";

support.focusin = "onfocusin" in window;

return support;

} );
