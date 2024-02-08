
const MyForm = class MyForm extends frappe.ui.form.Form {
	add_custom_button(label, fn, group){
        const button_check_map = frappe.button_check_map;
        if (button_check_map){
            const doctype_button = button_check_map[this.doctype];
            let check_doctype = doctype_button? doctype_button[label] : undefined;
            //Update Items in PO/SO toolbar button
            if (doctype_button && ! group && check_doctype &&
                (! frappe.model.can_write(check_doctype)) && (label in doctype_button || __(label) in doctype_button)){
                return
            }
            const all_button =button_check_map['All'];            
            if (check_doctype === undefined || !check_doctype){
                check_doctype = all_button && all_button[label]
            }
            if (check_doctype){
                if (group){
                    if (in_list([__('Create'), 'Create']), group){
                        if (! frappe.model.can_create(check_doctype)) return
                    }else if(in_list([__('View'), 'View']), group){
                        if (! frappe.model.can_read(check_doctype)) return
                    } 
                }
            }        
        }
        return super.add_custom_button(label, fn, group)
    }
}

frappe.ui.form.Form = MyForm
