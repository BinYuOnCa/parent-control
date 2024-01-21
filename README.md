# parent-control
Personal project to trace my kids screen time on computer.

Put the python script under following folder to enable it to be run by all users:
<code>
 C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
</ code>

tech points:

- get current login user info:
<code>
(base) PS C:\Users\All Users> Get-WmiObject -class Win32_ComputerSystem | Format-List Username

Username : DESKTOP-SNM5D0S\Ben


$u = (C:\Users\All Users> Get-WmiObject -class Win32_ComputerSystem | Format-List Username)

(base) PS C:\Users\All Users>
</ code>


- send email in Power Shell
<code>
user_info = Get-WmiObject -class Win32_ComputerSystem | Format-List Username
body = ''
Send-MailMessage -To yubin.on.ca@gmail.com -from yubin.dmd@gmail.com -Subject 'Desk-Login Log' -SmtpServer


Send-MailMessage -To '<recipient’s email address>' 
                -From '<sender’s email address>' 
                -Subject 'Your message subject' 
                -Body 'Some important plain text!' 
                -Credential (Get-Credential) 
                -SmtpServer '<smtp server>' 
                -Port 587

</ code>


Generated app password
Your app password for your device
ccja tlox pder idfn
How to use it
Go to the settings for your Google Account in the application or device you are trying to set up. Replace your password with the 16-character password shown above.
Just like your normal password, this app password grants complete access to your Google Account. You won't need to remember it, so don't write it down or share it with anyone.




$userName = 'yubin.dmd@gmail.com'
$password = 'ccja tlox pder idfn'
$securepassword = $password | ConvertTo-SecureString -AsPlainText -Force 
$credential = New-Object System.Management.Automation.PSCredential -ArgumentList $username, $securepassword
$subject = 'User Login notification'
$body = (Get-WmiObject -class Win32_ComputerSystem | Format-List Username) + (date)
Send-MailMessage -SmtpServer smtp.gmail.com -Port 587 -UseSsl -From yubin.dmd@gmail.com -To yubin.on.ca@gmail.com  -Subject $subject -Body $body -Credential $credential



