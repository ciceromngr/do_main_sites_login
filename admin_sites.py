#---------------------------------------------#
#---------------- CICERO ROMAO ---------------#
#---------------------------------------------#

import requests, sys, time, os

os.system('color 0a && cls')

print('+'*50)
print("++++++++++++++++++A+D+M+I+M+++++++++++++++++++++++") 
print('+'*50)

def formaDeUsarScript():
    print('\n')
    print('Uso: python admnin_sites.py http://site.exemplo')

if len(sys.argv) >= 2:
    print('\n Script Iniciado ............................\n')
    lista = ["admin.php","admin.html","login","w/index.php","index.php","login.php","login.html","administrator","admin","adminpanel","cpanel","login","wp-login.php","administrator","admins","logins","admin.asp","login.asp","adm/","admin/","admin/account.html","admin/login.html","admin/login.htm","admin/controlpanel.html","admin/controlpanel.htm","admin/adminLogin.html","admin/adminLogin.htm","admin.htm","admin.html","adminitem/","adminitems/","administrator/","administrator/login.","administrator.","administration/","administration.","adminLogin/","adminlogin.","admin_area/admin.","admin_area/","admin_area/login.","manager/","superuser/","superuser.","access/","access.","sysadm/","sysadm.","superman/","supervisor/","panel.","control/","control.","member/","member.","members/","user/","user.","cp/","uvpanel/","manage/","manage.","management/","management.","signin/","signin.","log-in/","log-in.","log_in/","log_in.","sign_in/","sign_in.","sign-in/","sign-in.","users/","users.","accounts/","accounts.","bb-admin/login.","bb-admin/admin.","bb-admin/admin.html","administrator/account.","relogin.htm","relogin.html","check.","relogin.","blog/wp-login.","user/admin.","users/admin.","registration/","processlogin.","checklogin.","checkuser.","checkadmin.","isadmin.","authenticate.","authentication.","auth.","authuser.","authadmin.","cp.","modelsearch/login.","moderator.","moderator/","controlpanel/","controlpanel.","admincontrol.","adminpanel.","fileadmin/","fileadmin.","sysadmin.","admin1.","admin1.html","admin1.htm","admin2.","admin2.html","yonetim.","yonetim.html","yonetici.","yonetici.html","phpmyadmin/","myadmin/","ur-admin.","ur-admin/","Server.","Server/","wp-admin/","administr8.","administr8/","webadmin/","webadmin.","administratie/","admins/","admins.","administrivia/","Database_Administration/","useradmin/","sysadmins/","sysadmins/","admin1/","system-administration/","administrators/","pgadmin/","directadmin/","staradmin/","ServerAdministrator/","SysAdmin/","administer/","LiveUser_Admin/","sys-admin/","typo3/","panel/","cpanel/","cpanel_file/","platz_login/","rcLogin/","blogindex/","formslogin/","autologin/","manuallogin/","simpleLogin/","loginflat/","utility_login/","showlogin/","memlogin/","login-redirect/","sub-login/","wp-login/","login1/","dir-login/","login_db/","xlogin/","smblogin/","customer_login/","UserLogin/","login-us/","acct_login/","bigadmin/","project-admins/","phppgadmin/","pureadmin/","sql-admin/","radmind/","openvpnadmin/","wizmysqladmin/","vadmind/","ezsqliteadmin/","hpwebjetadmin/","newsadmin/","adminpro/","Lotus_Domino_Admin/","bbadmin/","vmailadmin/","Indy_admin/","ccp14admin/","irc-macadmin/","banneradmin/","sshadmin/","phpldapadmin/","macadmin/","administratoraccounts/","admin4_account/","admin4_colon/","radmind-1/","Super-Admin/","AdminTools/","cmsadmin/","SysAdmin2/","globes_admin/","cadmins/","phpSQLiteAdmin/","navSiteAdmin/","server_admin_small/","logo_sysadmin/","power_user/","system_administration/","ss_vms_admin_sm/","bb-admin/","panel-administracion/","instadmin/","memberadmin/","administratorlogin/","adm.","admin_login.","panel-administracion/login.","pages/admin/admin-login.","pages/admin/","acceso.","admincp/login.","admincp/","adminarea/","admincontrol/","affiliate.","adm_auth.","memberadmin.","administratorlogin.","modules/admin/","administrators.","siteadmin/","siteadmin.","adminsite/","kpanel/","vorod/","vorod.","vorud/","vorud.","adminpanel/","PSUser/","secure/","webmaster/","webmaster.","autologin.","userlogin.","admin_area.","cmsadmin.","security/","usr/","root/","secret/","admin/login.","admin/adminLogin.","moderator.php","moderator.html","moderator/login.","moderator/admin.","yonetici.","0admin/","0manager/","aadmin/","cgi-bin/login","login1","login_admin/","login_admin","login_out/","login_out","login_user","loginerror/","loginok/","loginsave/","loginsuper/","loginsuper","login","logout/","logout","secrets/","super1/","super1","super_index","super_login","supermanager","superman","superuser","supervise/","supervise/Login","super"]
    try:
        for i in lista:
            url = sys.argv[1] + i
            r = requests.get(url)

            if r.status_code == 200:
                print('[+] PAGE FOUND: ' + url)
            else:
                print('....')
                pass
        print('\n Termino do programa: %s'% time.strftime('%H:%M:%S'))
    except KeyboardInterrupt:
        print('\n [x] Script Abortado: %s'% time.strftime('%H:%M:%S'))
    except:
        print("[x] Ocorreu algum erro na segmentacao ...")
        print("\n[-] OBS : O site poder conter alguma protecao, poder estar fora do ar,\n ou entao digite desta")
else:
    formaDeUsarScript()
