# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.query_builder import Case


@frappe.whitelist()
def get_button_check_map():         
    button_check = frappe.qb.DocType('Button Check')
    button_check_doctype = frappe.qb.DocType('Button Check DocType')
    button_check_button = frappe.qb.DocType('Button Check Button')
    for_doctype = Case().when(
                    button_check_doctype.for_doctype.isnull(), "All"
                ).else_(
                    button_check_doctype.for_doctype
                ).as_('for_doctype') 
    button_check_list = frappe.qb.from_(
            button_check
        ).join(
            button_check_button
        ).on(
            button_check_button.parent == button_check.name
        ).left_join(
            button_check_doctype
        ).on(
            button_check_doctype.parent == button_check.name
        ).distinct().select(
            for_doctype,
            button_check_button.button,
            button_check_button.check_doctype
        ).run()  

    button_map = frappe._dict()
    for (for_doctype, button, check_doctype) in button_check_list:
        record = button_map.setdefault(for_doctype, frappe._dict({button: check_doctype}))
        record[button] = check_doctype
        record[_(button)] = check_doctype
    return button_map    