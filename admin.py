import requests,os
os.system('clear')
admin = [
    '/admin.php', '/admin_page.php', '/admin_panel.php', '/admin-login.php',
    '/admin_area.php', '/admin_dashboard.php', '/admin_control.php', '/admin-access.php',
    '/admincp.php', '/adminpage.php', '/admin123.php', '/administrator.php', '/adminarea.php',
    '/adminhome.php', '/adminconsole.php', '/adminpanel.php', '/admin_portal.php',
    '/admin_site.php', '/adminweb.php', '/admin_login.php', '/admin_page.php', '/admin_panel.php',
    '/admin-login.php', '/admin_area.php', '/admin_dashboard.php', '/admin_control.php',
    '/admin-access.php', '/admincp.php', '/adminpage.php', '/admin123.php', '/administrator.php',
    '/adminarea.php', '/adminhome.php', '/adminconsole.php', '/adminpanel.php', '/admin_portal.php',
    '/admin_site.php', '/adminweb.php', '/login.php', '/panel.php', '/control.php',
    '/dashboard.php', '/console.php', '/site.php', '/web.php', '/index.php',
    '/home.php', '/administration.php', '/system.php', '/manage.php', '/admin1.php',
    '/admin2.php', '/admin3.php', '/admin4.php', '/admin5.php', '/usuarios.php',
    '/usuario.php', '/administrator/', '/moderator/', '/webadmin/', '/adminarea/',
    '/bb-admin/', '/adminLogin/', '/admin_area/', '/panel-administracion/', '/instadmin/',
    '/memberadmin/', '/administratorlogin/', '/adm/', '/admin/account.php', '/admin/index.php',
    '/admin/login.php', '/admin/admin.php', '/admin/account.php', '/admin_area/admin.php',
    '/admin_area/login.php', '/siteadmin/login.php', '/siteadmin/index.php', '/admin_area/index.php',
    '/bb-admin/index.php', '/bb-admin/login.php', '/bb-admin/admin.php', '/admin/home.php',
    '/admin_area/login.html', '/admin/index.html', '/admin/login.html', '/admin/admin.html',
    '/admin_area/admin.html', '/admin_area/index.html', '/admin_area/index.html', '/admin/cp.php',
    '/cp.php', '/administrator/index.php', '/administrator/login.php', '/nsw/admin/login.php',
    '/webadmin/login.php', '/admin/admin_login.php', '/admin_login.php', '/administrator/account.php',
    '/administrator.php', '/admin_area/admin.html', '/pages/admin/admin-login.php', '/admin/admin-login.php',
    '/admin-login.php', '/admin/admin_login.php', '/admin_area/index.php'
]
a=input('\033[36m[+]Enter the website link: ')
for site in admin:
	page=a+site
	r=requests.get(page)
	if r.status_code=='200':
		print('\033[92m'+page)
		break;
	else:
		continue
