// Copyright (c) 2025, Sigzen and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {
	enable: function(frm) {
        frm.call({
            doc :frm.doc,
            method: 'frm_call',
            args: {
                msg: "Hello"
            },
            freeze: true,
            freeze_massage: __('Calling frm_call Method'),
            callback: function(r) {
                // frappe.msgprint(r.message)

                // frappe.msgprint("Server Side calling Compleated")

                // frm.refresh_field('medicatoin_orders');
            }
        });
	},
});
