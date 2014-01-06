import pytz



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
  u'from': u'"Scott Coates" <lkdfslk0804@reply.craigslist.org>', u'attachments': u'0',
  u'to': u'slkdfuiu-aslkj@hous.craigslist.org',
  u'text': u'''
Hello,
Is this apartment still available? Could I view Thursday around 6-7pm?
Thanks look forward to hearing from you.
-Some Dude


http://newyork.craigslist.org/mnh/abo/123456789.html


------------------------------------------------------------------------
Original craigslist post:
http://newyork.craigslist.org/mnh/abo/123456789.html
About craigslist mail:
http://craigslist.org/about/help/email-relay
Please flag unwanted messages (spam, scam, other):
http://craigslist.org/mf/abc123456789.1
------------------------------------------------------------------------
''',
  u'envelope': u'''{
  "from":"some_test_acct+caf_=info=romoh.com@gmail.com",
  "to":[
    "fake_third_party@gmail.com"
  ]
}
''',
  u'headers': u'''Received: by mx-004.sjc1.sendgrid.net with SMTP id 18dHlq6tsM Thu, 02 Jan 2014 23:13:24 +0000 (GMT)
Received: from mail-lb0-f175.google.com (mail-lb0-f175.google.com [209.85.217.175]) by mx-004.sjc1.sendgrid.net (Postfix) with ESMTPS id 0F1041055157 for <fake_third_party@gmail.com>; Thu,  2 Jan 2014 23:13:23 +0000 (GMT)
Received: by mail-lb0-f175.google.com with SMTP id w6so7603659lbh.6 for <fake_third_party@gmail.com>; Thu, 02 Jan 2014 15:13:22 -0800 (PST)
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=1e100.net; s=20130820; h=x-original-authentication-results:delivered-to:from:to:subject:date :content-type:mime-version:message-id; bh=Om1Z1vu4QlqFnE4peeRdaxKRO9ermLxCchcXPpknK8s=; b=jlQmIOvcz1I5bO4A3SQH5r6vknst0toNPv7MEPkX4ZMJcgAwGAcc9nwCemyrokGmYp G0j4eXC/V0kWASUyzPCW61Ry3WXWoHrv0MNplLhgDwqptY/662mKtNJlFa/zBjbmaurA caoTvuSPCbkB927miHrAWczRsYI9OxnM5xxiU+edudwa4tkiGyJkLlW0kF9sbJjP1KqJ rZY2NKhKWuq9em+pm2yOpAJjs9y7M4bPNdJ1TpWb5cUW3gVqpEok3IM96wxq8xbAZFq7 qEP0SDNq3AgxLjbY2cfpf6x03P1jYdGeGn8RRJQhpnUBm3t0NTRofTEOvaAzHntO22jS g1JQ==
X-Original-Authentication-Results: mx.google.com;       spf=pass (google.com: domain of bounce-anon-some_test_acct=gmail.com@craigslist.org designates 208.82.236.98 as permitted sender) smtp.mail=bounce-anon-some_test_acct=gmail.com@craigslist.org
X-Received: by 10.112.180.37 with SMTP id dl5mr3644516lbc.58.1388704402192; Thu, 02 Jan 2014 15:13:22 -0800 (PST)
X-Forwarded-To: fake_third_party@gmail.com
X-Forwarded-For: some_test_acct@MarketTest1.com fake_third_party@gmail.com
Delivered-To: some_test_acct@MarketTest1.com
Received: by 10.112.5.198 with SMTP id u6csp479511lbu; Thu, 2 Jan 2014 15:13:21 -0800 (PST)
X-Received: by 10.224.103.68 with SMTP id j4mr32108754qao.95.1388704401254; Thu, 02 Jan 2014 15:13:21 -0800 (PST)
Received: from mxo3p.int.craigslist.org (mxo3p.craigslist.org. [208.82.236.98]) by mx.google.com with ESMTP id j9si56257207qec.107.2014.01.02.15.13.20 for <some_test_acct@MarketTest1.com>; Thu, 02 Jan 2014 15:13:21 -0800 (PST)
Received-SPF: pass (google.com: domain of bounce-anon-some_test_acct=gmail.com@craigslist.org designates 208.82.236.98 as permitted sender) client-ip=208.82.236.98;
Authentication-Results: mx.google.com; spf=pass (google.com: domain of bounce-anon-some_test_acct=gmail.com@craigslist.org designates 208.82.236.98 as permitted sender) smtp.mail=bounce-anon-some_test_acct=gmail.com@craigslist.org
From: "Scott Coates" <lkdfslk0804@reply.craigslist.org>
To: slkdfuiu-aslkj@hous.craigslist.org
Subject: NO Fee Gorgeous Furnished High Floor nice View
Date: Thu, 2 Jan 2014 18:13:01 -0500
X-CL-ID: DF69663F-B5BF-4825-B4DF-225F42FCF768.1
Content-Type: multipart/alternative; boundary="CraigslistMail-v1-50411E24-587C-38C1-9063-4884D62889CB"
MIME-Version: 1.0
Message-Id: <l3GzG4byedMjIymhC6t7SlbsggkLEJeVUPoDK5lrF-K8J8cQ4DZZQbR7NST4C-Oc31nKj03mCBuxld92FzBVtn9e5cPNXwP5EqRwJ0aiXgg@v2.cl.com>
''',
  u'html': u'''
    <div dir=3D"ltr"><span style=3D"font-size:13px;font-family:arial,sans-serif=
  ">Hello,</span><div style=3D"font-size:13px;font-family:arial,sans-serif">I=
  s this apartment still available? Could I view Thursday around 6-7pm? Thank=
  s look forward to hearing from you.</div>
  <div style=3D"font-size:13px;font-family:arial,sans-serif">-Some Dude</div><d=
  iv><br></div><br><a href=3D"http://newyork.craigslist.org/mnh/abo/123456789=
  3.html">http://newyork.craigslist.org/mnh/abo/1234567893.html</a><br></div>
  <br>
  <hr>Original craigslist post:<br>
  <a href=3D"http://newyork.craigslist.org/mnh/abo/1234567893.html">http://ne=
  wyork.craigslist.org/mnh/abo/1234567893.html</a><br>
  About craigslist mail:<br>
  <a href=3D"http://craigslist.org/about/help/email-relay">http://craigslist.=
  org/about/help/email-relay</a><br>
  Please flag unwanted messages (spam, scam, other):<br>
  <a href=3D"http://craigslist.org/mf/abc1297654=
  2.1">http://craigslist.org/mf/abc123456789.1</a=
  ><hr>=
''',
  u'charsets': u'{"to":"UTF-8","cc":"UTF-8","html":"ISO-8859-1","subject":"UTF-8","from":"UTF-8","text":"ISO-8859-1"}',
  u'dkim': u'{@gmail.com : pass}', u'SPF': u'pass', u'subject': u'Hi'
}

eastern_time_zone = pytz.timezone('US/Eastern')

# region result 1
search_1 = {
  'description': 'I want a great place to live',
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
