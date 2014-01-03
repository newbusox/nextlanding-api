import pytz

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

email_2 = {
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
  u'text': u'This is a test, okay\r\n',
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
  u'html': u'<div dir="ltr">This is a test, okay</div>\r\n',
  u'charsets': u'{"to":"UTF-8","cc":"UTF-8","html":"ISO-8859-1","subject":"UTF-8","from":"UTF-8","text":"ISO-8859-1"}',
  u'dkim': u'{@gmail.com : pass}', u'SPF': u'pass', u'subject': u'Hi'
}

eastern_time_zone = pytz.timezone('US/Eastern')

# region result 1
search_1 = {
  'description': 'I want a great place to live',
  'email_address': 'test@test.com',
  'specified_location': 'Astoria NY',
  'geo_boundary_points': {"0": [[40.738152838822934, -74.0741103887558], [40.717338733312495, -74.05419766902924],
                                [40.701463603604594, -74.08990323543549]]},
  'no_fee_preferred': True,
  'bedroom_max': 2,
  'bathroom_max': 1.5,
  'sqfeet_max': 850.50,
  'price_max': 2500.50,
  'amenities': [1, 2]
}

cl_listing_4033538277 = {u'city': [u'brooklyn'], u'contact_phone_number': [u'bedstuy / clinton hill'],
                         u'description': [u'\n\t\tBeautiful 3 Bedroom 2 Full bath', u'\nAmazing Finishes',
                                          u'\nHuge Backyard',
                                          u'\n100% no fee By owner',
                                          u'\nAll Bedrooms can fit King and Queen sized beds',
                                          u'\nSteps to the G train', u'\nLaundry in the Building',
                                          u'\nClose to All your needs',
                                          u'\nNo brokers Please', u'\nCall or Text Danny @ 646 338 3852 ',
                                          u'\n3526+56+5\n\t'],
                         u'title': [
                           u'\n  - $2695 / 3br - 3 Bedroom 2 Full bath + Massive Backyard~Prime Location (bedstuy / '
                           u'clinton hill)\n'],
                         u'url': u'http://newyork.craigslist.org/brk/abo/4033538277.html', u'state': [u'ny'],
                         u'last_updated_date': [],
                         u'posted_date': [u'2013-08-29, 12:55PM EDT', u'2013-08-29, 12:55PM EDT'],
                         u'contact_email_address': [u'test@hous.craigslist.org'],
                         u'address': [u'vernon ave at nostrand', u'vernon ave', u'nostrand'], u'lat': [u'40.694263'],
                         'listing_source_id': 1,
                         u'lng': [u'-73.952341'], u'broker_fee': [u'/brk/abo/4033538277.html'],
                         u'contact_name': [u'bedstuy / clinton hill']}

#endregion
