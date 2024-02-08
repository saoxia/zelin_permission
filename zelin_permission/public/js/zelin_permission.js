$(document).on('app_ready', function() {
	if (document.referrer.endsWith("/login")) {
		// app ready after login, let's rumble
		//console.log("zelin permission after login event trigger");
		// get persistent session settings
		frappe.call({
			'method': "zelin_permission.api.get_button_check_map",
			'callback': function(response) {
				if (response.message) {
					//console.log(response.message);
                    frappe.button_check_map = response.message;
				}
			}
		});
	}
});