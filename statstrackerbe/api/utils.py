from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags


def send_welcome_email(to_email, fullname):
    subject = f"{fullname}, שאלון ההתאמה שלך נשלח בהצלחה!"
    message_html = f"""
    <html>
        <body>
                <p>!{fullname}, שאלון ההתאמה נשלח אלינו</p>
                <p>.נעבוד על התוכנית אימונים והתפריט תזונה שלך בהקדם האפשרי</p>
                <p>.אם יש שאלות כמובן שאני תמיד זמין</p>
                <p>!שימו לב לא לשכוח למלא את השאלון עדכון מתי שצריך כדי שנוכל לעדכן גם את התוכניות</p>            
        </body>

         <style>@import url('https://fonts.googleapis.com/css?family=Oxygen');</style>
        <table style="width:400px; height: 213px; padding-top:33px; padding-right:0; padding-bottom:38px; padding-left:10px; font-family: 'Oxygen', sans-serif; font-size: 12px">
        <tbody>
            <tr>
            <td style="width:110px; padding:0;">
                <img src="https://cdn.discordapp.com/attachments/1080799589982031924/1270859670432649366/logo.png?ex=66b53bcc&is=66b3ea4c&hm=38a8a7bbd8a9dc2355fe265f11508b82bf2993344d8e6ac768c899d0e44e33fc&" alt="הלוגו שלנו" style="width:100px; opacity: 0.8; border-radius: 33%; background: #121212;">
                <br>
                <br>
                <a href="https://www.tiktok.com/@micha.stocks"><img src="https://img.icons8.com/?size=32&id=118638&format=png" width=16px alt="TikTok Link" style="padding-left:14px;"></a>
                <a href="https://facebook.com/100084129517900/"><img src="https://img.icons8.com/?size=32&id=13912&format=png" width=16px alt="Facebook Link"></a>
                <a href="https://www.youtube.com/@Micha.Stocks"><img src="https://img.icons8.com/?size=32&id=13983&format=png" width=16px alt="Youtube Link" ></a>
                <a href="https://www.instagram.com/micha.stocks"><img src="https://img.icons8.com/?size=32&id=Xy10Jcu1L2Su&format=png" width=16px alt="Instagram Link"></a>
            </td>
            <td style="border-left: 2px solid #121212; width:22px; height:136px; padding: 0px; opacity:0.8"></td>
            <td style="padding:0px">
                <b>NL Fitness Tracker</b>
                <br>
                <a href="tel:050-990-3991" style="text-decoration:none; color:black;"><img src="https://img.icons8.com/?size=32&id=0k3RLElvAdsE&format=png"  height=10px alt="Phone Icon"> 050-990-3991</a>
                <br>
                <a href="NLFitnessTracker.co.il" style="text-decoration:none; color:black;"><img src="https://img.icons8.com/?size=32&id=1lsm7jKm7MeX&format=png"  height=10px alt="Website Link Icon"> NLFitnessTracker.co.il</a>
            </td>
            </tr>
        </tbody>
        </table>
    </html>
    """

    message_plain = strip_tags(message_html)
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [to_email]

    send_mail(
        subject, message_plain, email_from, recipient_list, html_message=message_html
    )


def send_which_user_filled_questionnaire(fullname):
    subject = f"{fullname} מילא את השאלון"
    message = f"{fullname} מילא את השאלון וניתן לראות את המידע שלו בפלטפורמה"
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = ["NLFitnessTracker@gmail.com"]

    send_mail(subject, message, email_from, recipient_list)


def send_contact_us_email_to_client(full_name, email):
    subject = f"{full_name} תודה שיצרת איתנו קשר!"
    message_html = f"""
    <html>
        <body>
                <p>!{full_name}, תודה שיצרת קשר איתנו</p>
                <p>.ניצור איתך קשר ברגע שנוכל</p>     
        </body>

         <style>@import url('https://fonts.googleapis.com/css?family=Oxygen');</style>
        <table style="width:400px; height: 213px; padding-top:33px; padding-right:0; padding-bottom:38px; padding-left:10px; font-family: 'Oxygen', sans-serif; font-size: 12px">
        <tbody>
            <tr>
            <td style="width:110px; padding:0;">
                <img src="https://cdn.discordapp.com/attachments/1080799589982031924/1270859670432649366/logo.png?ex=66b53bcc&is=66b3ea4c&hm=38a8a7bbd8a9dc2355fe265f11508b82bf2993344d8e6ac768c899d0e44e33fc&" alt="הלוגו שלנו" style="width:100px; opacity: 0.8; border-radius: 33%; background: #121212;">
                <br>
                <br>
                <a href="https://www.tiktok.com/@micha.stocks"><img src="https://img.icons8.com/?size=32&id=118638&format=png" width=16px alt="TikTok Link" style="padding-left:14px;"></a>
                <a href="https://facebook.com/100084129517900/"><img src="https://img.icons8.com/?size=32&id=13912&format=png" width=16px alt="Facebook Link"></a>
                <a href="https://www.youtube.com/@Micha.Stocks"><img src="https://img.icons8.com/?size=32&id=13983&format=png" width=16px alt="Youtube Link" ></a>
                <a href="https://www.instagram.com/micha.stocks"><img src="https://img.icons8.com/?size=32&id=Xy10Jcu1L2Su&format=png" width=16px alt="Instagram Link"></a>
            </td>
            <td style="border-left: 2px solid #121212; width:22px; height:136px; padding: 0px; opacity:0.8"></td>
            <td style="padding:0px">
                <b>NL Fitness Tracker</b>
                <br>
                <a href="tel:050-990-3991" style="text-decoration:none; color:black;"><img src="https://img.icons8.com/?size=32&id=0k3RLElvAdsE&format=png"  height=10px alt="Phone Icon"> 050-990-3991</a>
                <br>
                <a href="NLFitnessTracker.co.il" style="text-decoration:none; color:black;"><img src="https://img.icons8.com/?size=32&id=1lsm7jKm7MeX&format=png"  height=10px alt="Website Link Icon"> NLFitnessTracker.co.il</a>
            </td>
            </tr>
        </tbody>
        </table>
    </html>
    """
    message_plain = strip_tags(message_html)
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(
        subject, message_plain, email_from, recipient_list, html_message=message_html
    )


def send_contact_us_email_to_us(full_name, email, phone, content):
    subject = f"{full_name} מילא את השאלון"
    if len(content) > 0:
        content = f"<p>{content} :טקסט שהם רשמו</p>"
    message_html = f"""
    <html>
        <body>
                <p>!{full_name} יצר איתנו קשר</p>
                <p>:פרטים</p>     
                <p>{email} :אימייל</p>     
                <p>{phone} :מס' פלאפון</p>     
                {content}     
        </body>
    </html>
    """
    message_plain = strip_tags(message_html)
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = ["NLFitnessTracker@gmail.com"]

    send_mail(
        subject, message_plain, email_from, recipient_list, html_message=message_html
    )
