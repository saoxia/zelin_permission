from . import __version__ as app_version

app_name = "zelin_permission"
app_title = "Permission Enhancement"
app_publisher = "Fisher"
app_description = "Permission Enhancement"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "yuxinyong@163.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zelin_permission/css/zelin_permission.css"
# app_include_js = "/assets/js/zelin_permission.min.js"
app_include_js = ["zelin_permission.bundle.js"]

# include js, css files in header of web template
# web_include_css = "/assets/zelin_permission/css/zelin_permission.css"
# web_include_js = "/assets/zelin_permission/js/zelin_permission.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "zelin_permission/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "zelin_permission.install.before_install"
# after_install = "zelin_permission.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zelin_permission.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Project": "zelin_permission.permission.project_query_conditions",
	"Task": "zelin_permission.permission.task_query_conditions"
}

has_permission = {
 	"Project": "zelin_permission.permission.has_permission",
	"Task": "zelin_permission.permission.has_permission"
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zelin_permission.tasks.all"
# 	],
# 	"daily": [
# 		"zelin_permission.tasks.daily"
# 	],
# 	"hourly": [
# 		"zelin_permission.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zelin_permission.tasks.weekly"
# 	]
# 	"monthly": [
# 		"zelin_permission.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "zelin_permission.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
	# 白名单覆盖只适用于来自外部网页或第三方应用经主控程序的白名单方法调用，不适用于像报表导出内部调用run方法，改猴子补丁实现
	#"frappe.desk.query_report.run": "zelin_permission.override.run_wrapper",
	"frappe.desk.query_report.get_data_for_custom_field":"zelin_permission.override.get_data_for_custom_field_wrapper"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zelin_permission.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"zelin_permission.auth.validate"
# ]

