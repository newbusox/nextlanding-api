email_1 = {
  u'spam_score': u'0.101',
  u'spam_report': u'Spam detection software, running on the system "mx3.sendgrid.net", '
                  u'has\r\nidentified this incoming email as possible spam.  The original message\r\nhas been '
                  u'attached to this so you can view it (if it isn\'t spam) or label\r\nsimilar future email.  If you'
                  u' have any questions, see\r\nthe administrator of that system for details.\r\n\r\nContent preview:'
                  u'  This is a test, okay This is a test, okay ... \r\n\r\nContent analysis details:   (0.1 points, '
                  u'5.0 required)\r\n\r\n pts rule name              description\r\n---- ---------------------- '
                  u'--------------------------------------------------\r\n 0.0 FREEMAIL_FROM          Sender email is'
                  u' commonly abused enduser mail provider\r\n                            (scott.c.coatesatgmail'
                  u'.com)\r\n-1.9 BAYES_00               BODY: Bayes spam probability is 0 to 1%\r\n                 '
                  u'           score: 0.0000\r\n 0.0 HTML_MESSAGE           BODY: HTML included in message\r\n 2.0 '
                  u'MIME_NO_TEXT           No (properly identified) text body parts\r\n\r\n',
  u'from': u'Scott Coates <scott.c.coates@gmail.com>', u'attachments': u'0',
  u'to': u'Some Guy <dude@garbagetracker.com>, someone@somewhere.net', u'cc': u'ccuser@cctest.com',
  u'text': u'This is a test, okay\r\nres-id: 1\r\n',
  u'envelope': u'{"to":"dude@garbagetracker.com","from":"scoarescoare@gmail.com"}',
  u'headers': u'Received: by 127.0.0.1 with SMTP id 82yyH0rXMn Wed, 18 Sep 2013 13:19:42 -0500 (CDT)\r\nReceived: '
              u'from mail-wi0-f169.google.com (mail-wi0-f169.google.com 209.85.212.169) by mx3.sendgrid.net (Postfix)'
              u' with ESMTPS id 1728814E173D for <dude@garbagetracker.com>; Wed, '
              u'18 Sep 2013 13:19:41 -0500 (CDT)\r\nReceived: by mail-wi0-f169.google.com with SMTP id '
              u'hj3so6790063wib.0 for <dude@garbagetracker.com>; Wed, 18 Sep 2013 11:19:41 -0700 ('
              u'PDT)\r\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=gmail.com; s=20120113; '
              u'h=mime-version:sender:date:message-id:subject:from:to:cc:content-type; '
              u'bh=x6iFLZEfsi3q/M7JR1K7Mi6vJPXgBQMYpo85Bo8IkKg=; '
              u'b=eC5rmQg0UzlR53mVM0YaFKB34gblaZ7hx7eg2zN1vda2hpsrwl2/GSIm0SfSor5poj '
              u'8BVXmCtuo3QbjvXaU6efRjfKGCBV/2ZFAxDyf5kiQLPAtjeVpLFVOdQuNRmUHxqIN5XA '
              u'UuFT5EytOxsoY5nBAKNYs5xe0NizdRDPWxiNPIqraRNYIjatEv1+Rj/pyKia8sVfN1Qv '
              u'ajgkQSXjFylJIDyqI24Q8X4Ek2XDEZ7juHfB34nRc++OPr6oOkLUaL2aTr3Ps//NB+I8 '
              u'4etKKZ4eboT1qG8z38tPMsBkeAGTyZWkT6IOfJ1BUFF+XLTgyEh/Q33jTnaVnvzGZOw0 mYRg==\r\nMIME-Version: 1'
              u'.0\r\nX-Received: by 10.180.11.37 with SMTP id n5mr8183272wib.25.1379528380941; Wed, '
              u'18 Sep 2013 11:19:40 -0700 (PDT)\r\nSender: scoarescoare@gmail.com\r\nReceived: by 10.194.78.82 with '
              u'HTTP; Wed, 18 Sep 2013 11:19:40 -0700 (PDT)\r\nDate: Wed, '
              u'18 Sep 2013 14:19:40 -0400\r\nX-Google-Sender-Auth: zE8IiRZJXpGBooQRsyrcfg-Szf8\r\nMessage-ID: '
              u'<CAKGSGYxmaQ-g-hRrOnBTRm6XVRn0VwFbfzgmc8mw+rgeDR+bvg@mail.gmail.com>\r\nSubject: Hi\r\nFrom: Scott '
              u'Coates <scott.c.coates@gmail.com>\r\nTo: Some Guy <dude@garbagetracker.com>, '
              u'someone@somewhere.net\r\nCc: ccuser@cctest.com\r\nContent-Type: multipart/alternative; '
              u'boundary=001a11c25b481a923c04e6ac7bd0\r\n',
  u'html': u'<div dir="ltr">This is a test, okay</div>\r\nres-id: 1\r\n',
  u'charsets': u'{"to":"UTF-8","cc":"UTF-8","html":"ISO-8859-1","subject":"UTF-8","from":"UTF-8","text":"ISO-8859-1"}',
  u'dkim': u'{@gmail.com : pass}', u'SPF': u'pass', u'subject': u'Hi'
}
