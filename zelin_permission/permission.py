import frappe


def has_permission(doc, ptype="read", user=None):
    def is_shared():
        shared = frappe.share.get_shared(doctype, user, [ptype])
        return doc.name in shared

    def is_member():
        result = True
        if doctype == 'Project':
            result = user in {row.user for row in doc.users}
        return result

    user = user or frappe.session.user
    doctype = doc.doctype
    if ptype=="create" or not doc.is_private or doc.owner == user:
        ret = True
    elif ptype in ('write','submit','share','delete'):
        ret = is_member() or is_shared()
    else:
        ret = bool(frappe.get_list(doctype, filters = {'name': doc.name}))
    return ret

def project_query_conditions(user):
    #项目创建者，系统管理员用户，管理员账号，公开项目不过滤
    conditions = ""
    special_user = ("System Manager"  in frappe.get_roles(user)) or (user =="Administrator")
    if not special_user:
        #获取作为项目成员的项目清单
        allowed_projects = frappe.get_all('Project User', filters ={'user': user}, pluck='parent')
        name_condition = ""
        if allowed_projects:
            name_condition = " or tabProject.name in (%s)" %(','.join(["'%s'" % c for c in allowed_projects]))
        conditions = '(tabProject.owner="%s" or tabProject.is_private = 0) %s' %(user, name_condition)  
    return conditions  

def task_query_conditions(user):
    #项目创建者，系统管理员用户，管理员账号，公开项目不过滤
    conditions = ""
    special_user = ("System Manager"  in frappe.get_roles(user)) or (user =="Administrator")
    if not special_user:
        #获取作为项目成员的项目清单
        allowed_projects = frappe.get_all('Project User', filters ={'user': user}, pluck='parent')
        name_condition = ""
        if allowed_projects:
            name_condition = " or tabTask.project in (%s)" %(','.join(["'%s'" % c for c in allowed_projects]))
        conditions = '(tabTask.owner="%s" or tabTask.is_private = 0) %s' %(user, name_condition)
    return conditions     