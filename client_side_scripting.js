// Copyright (c) 2025, Sigzen and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Client Side Scripting", {

// 	refresh: function(frm) {
//         console.log("Hello");
//         frappe.msgprint("Hello Dev from 'refresh' event ")    
// 	},

    // onload: function(frm){
    //     frappe.msgprint("Hello Dev from 'onload' event") 
    // }

    // validate: function(frm){
    //     frappe.throw("Hello Dev from 'validate' event") 
    // }
    
    // before_save: function(frm){
    //     frappe.throw("Hello Dev from 'before_save' event") 
    // }
    
    // after_save: function(frm){
    //     frappe.throw("Hello Dev from 'after_save' event") 
    // }

   	// enable: function(frm) {
    //     frappe.msgprint("Hello Dev from 'enable' fieldname event")    
	// },

	// age: function(frm){
    //     console.log("tyr75dtfgvbh")
    //     frappe.msgprint("Hello Dev from 'age' ")
    // }

    // family_member_on_form_rendered: function(frm)
    // {
    //     frappe.msgprint("Hello Dev from 'family_member' child table rendered event")
    // }

    // before_submit: function(frm){
    //     frappe.throw("Hello Dev from 'before_submit' event")
    // }

    // on_submit: function(frm){
    //     frappe.msgprint("Hello Dev from 'on_submit' event")
    // }

    // before_cancel: function(frm)
    // {
    //     frappe.throw("Hello Dev from 'before_cancel' event")
    // }

    // after_cancel: function(frm)
    // {
    //     frappe.msgprint("Hello Dev from 'after_cancel' event")
    // }
    
// }); 



// frappe.ui.form.on('Client Side Scripting', {

// });    

    // additional validation on Task dates
    // frappe.ui.form.on('Family Member', {

    //     age: function(frm) {
    //     // if (frm.doc.from_date < get_today()) {
    //         frappe.msgprint('Hello Dev from Child DocType fieldname avent')
    //     // }
    //     }
    // })
 




// frappe.ui.form.on('Family Member', {
        
//         age(frm, cdt, cdn) {
//             frappe.msgprint("Hello Dev from 'age' Child DocType fieldname avent")

//         }
//     })




// frappe.ui.form.on('Client Side Scripting',  {
     


//      // frm.doc.first_name


//     after_save: function(frm) {
//         frappe.msgprint(__("The full name is '{0}'",
//             [frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name]
//         ))

//         for (let row of frm.doc.family_member) {
//             frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}'",
//                 [row.idx,row.name1,row.relation]))
//         }    
//     }
// });





// frappe.ui.form.on('Client Side Scripting',  {

//     refresh:function(frm){
//         // frm.set_intro('Now you can create a new Client Side Scripting doctype')

//         if(frm.is_new()) {
//             frm.set_intro('Now you can create a new Client Side Scripting doctype')
//         }
//     }
// });




// frappe.ui.form.on('Client Side Scripting',  {

//     validate:function(frm){
//         // frm.set_value('full_name',frm.doc.first_name +" "+ frm.doc.middle_name+" "+frm.doc.last_name)
//         let row = frm.add_child('family_member', {
//             name1: 'Dev',
//             relation: 'Father',
//             age: 32,
//         })
//     }


// });




// frappe.ui.form.on('Client Side Scripting',  {
//     enable:function(frm){

    
//         // frm.set_df_property('first_name', 'reqd',1)

//         // frm.set_df_property('middle_name','read_only',1)

//         frm.toggle_reqd('age',true)
//     }
// });





// frappe.ui.form.on('Client Side Scripting',  {

//     refresh:function(frm) {
//         // frm.add_custom_button('Click Me Button',() => {
//         //     frappe.msgprint(__('You Clicked Me!!'));
//         // })

//         frm.add_custom_button('Click Me1',() =>{
//             frappe.msgprint(__('You Clicked 1 !! '));
//         },'click me')

        
//         frm.add_custom_button('Click Me2',() =>{
//             frappe.msgprint(__('You Clicked 2 !! '));
//         },'click me')
//     }
// });

