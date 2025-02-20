    # Copyright (c) 2025, Sigzen and contributors
    # For license information, please see license.txt

    # import frappe
    # from frappe import _
    # from frappe.model.document import Document


    # class ServerSideScripting(Document):

    # def validate(self):
    # 	frappe.msgprint("Hello Frappe from 'validate' Event ")

    # def before_save(self):
    # 	frappe.throw("Hello Frappe from'before_save' Event ")

    # def before_insert(self):
    # 	frappe.throw("Hello Frappe from 'before_insert' Event")

    # def after_insert(self):
    # 	frappe.throw("Hello Frappe from 'after_insert' Event")

    # def on_update(self):
    # 	frappe.msgprint("Hello Frappe from 'on_update' Event")

    # def before_submit(self):
    # 	frappe.msgprint("Hello Frappe from 'before_submit' Event")

    # def on_submit(self):
    # 	frappe.msgprint("Hello Frappe from 'on_submit' Event") 

    # def on_cancel(self):
    # 	frappe.msgprint("Hello Frappe from 'on_cancel' Event") 

    # def on_trash(self):
    # 	frappe.msgprint("Hello Frappe from 'on_trash' Event") 

    # def after_delete(self):
    # 	frappe.msgprint("Hello Frappe from 'after_delete' Event") 

    ########################## Value Fetching ########################


# import frappe
# from frappe import _
# from frappe.model.document import Document


# class ServerSideScripting(Document):



    # def validate(self):
    # 	frappe.msgprint(_("Hello My full name is '{0}' ").format(
    # 		self.first_name +" "+ self.middle_name +" "+ self.last_name))
        
    # def validate(self):
    # 	for row in self.get("family_member"):
    # 		frappe.msgprint(_(
    # 			"{0}. The Family Member name is '{1}' and relation is '{2}' ").format(
    # 				row.idx,row.name1,row.relation))

    #####################frappe.get_doc(doctype, name) #################
    # Return a Document object of the record identified by doctype and name

    # frappe.get_doc(doctype, name)

    # def validate(self):
    # 	self.get_document()

    # def get_document(self):
    # 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
    # 	frappe.msgprint(_("The First Name is {0} and Age is {1}").format(doc.first_name,doc.age))

    # 	for row in doc.get("family_member"):
    # 		frappe.msgprint(_(
    # 			"{0}. The family member name is '{1}' and relation is '{2}'").format(
    # 			row.idx,row.name1,row.relation))



    # def validate(self):
    # 	self.new_document()

    # def new_document(self):
    # 	doc =  frappe.new_doc('Client Side Scripting')
    # 	doc.first_name = 'Dev'
    # 	doc.last_name = 'Radadiya'
    # 	doc.age = 21
    # 	doc.append("family_member",{  "name1":"jemi",
    #                           		  "relation":"Sister",
    #                               	  "age": 15
    #                                  })

    # 	doc.insert()

    # Frappe.delete_doc(doctype,name)

    # def validate(self):
    # 	frappe.delete_doc('Client Side Scripting', 'PR-0003')



    ###### doc.insert()

    # def validate(self):
    # 	self.new_document()
        
    # def new_document(self):
    # 	doc = frappe.new_doc('Client Side Scripting')
    # 	doc.first_name = 'Jelly'
    # 	doc.age = 16
    # 	doc.insert()

    # doc.insert(
    # 	ignore_permitiond=True,
    # 	ignore_links=True,
    # 	ignore_if_duplicate=True,
    # 	ignore_mandatory=True
    # )

    ### doc.save()

    # def validate(self):
    # 	self.save_document()

    # def save_document(self):
    # 	doc = frappe.new_doc('Client Side Scripting')
    # 	doc.first_name = 'bunny'
    # 	doc.age = 65
    # 	doc.save()

    # 	doc.save(
    # 		ignore_permissions=True,
    # 		ignore_version=True
    # 	)
    #doc.delete()

    # def validate(self):
    # 	self.delete_document()

    # def delete_document(self):
    # 	doc = frappe.get_doc('Client Side Scripting', 'PR-0011')
    # 	doc.delete()

    ### doc.db_set()


    # def validate(self):
    # 	self.db_set_document()

    # def db_set_document(self):
    # 	doc = frappe.get_doc('Client Side Scripting', 'PR-0012')
    # 	doc.db_set('age', 45)


    # # frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

        # def validate(self):
        # 	self.get_list()

        # def get_list(self):
        #     doc = frappe.db.get_list('Client Side Scripting',
        #             filters={
        #                 'enable' : 1
        #             },
        #             fields=['first_name','age']
        #             )
        #     for d in doc:
        #         frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format('d.first_name,d.age'))


###It is use to find enable child doctype names#### 


  
    # def validate(self):
    #     self.get_list()
        
    # def get_list(self):
    #     doc = frappe.db.get_list('Client Side Scripting',
    #                              filters= {
    #                                  'enable': 1
    #                              },
    #                              fields=['first_name', 'age']
    #                              )
    #     for d in doc:
    #         frappe.msgprint(("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))




import frappe
from frappe import _
from frappe.model.document import Document


class ServerSideScripting(Document):
    
# frappe.db.get_value(document, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)

    # def validate(self):
    #     self.get_value()
        
    # def get_value(self):
    #     first_name,age = frappe.db.get_value('Client Side Scripting', 'PR-0012', ['first_name,age'])
    #     frappe.msgprint(_("The Parent First Name is{0} and age is {1} ").format(first_name,age))
    
################################

    # def validate(self):
    #     self.set_value()
        
    # def set_value(self):
    #     frappe.db.set_value('Client Side Scripting','PR-0012','age',25)
        
    # first_name, age = frappe.db.get_value('Client Side Scripting','PR-0012',['first_name','age'])
    # frappe.msgprint(_("The Perent First Name is {0} and new age is {1}").format(first_name,age))
    
    
    
    
###########################
    # def validate(self):
    #     if frappe.db.exists('Client Side Scipting','PR-0016'):
    #         frappe.msgprint(_("The Document is Exists in Database"))
    #     else:
    #         frappe.msgprint(_("The Document does not Exists in Database"))
            
        
################################ check how many enables are there

    # def validate(self):
    #     doc_count = frappe.db.count('Client Side Scripting', {'enable': 1})
    #     frappe.msgprint(_("The Enable Document Count is {0}").format(doc_count))
        

################################

    # def validate(self):
    #     self.sql()
        
    # def sql(self):
    #     data = frappe.db.sql("""
    #                             SELECT
    #                                 first_name,
    #                                 age
    #                             FROM
    #                                 `tabClient Side Scripting`
    #                             WHERE
    #                                 enable = 1
    #                         """, as_dict=1)
    #     for d in data:
    #         frappe.msgprint(_("The Parent First Name is {0} and Age is {1}").format(d.first_name,d.age))
            
#######################time.sleep is use to freeze time for hoe many sec you want
    @frappe.whitelist()
    def frm_call(self,msg):
        import time
        time.sleep(5)
        
        #it is basically use to give massage from js code
        frappe.msgprint(msg)
        
        # self.mob_no= 77677656
        
        # return "Hi This Message from frm_call"
