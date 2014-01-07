import textwrap


BUYER_PURCHASE_SUBJECT_TEMPLATE = "Nextlanding: Search Complete"
BUYER_PURCHASE_BODY_TEMPLATE = textwrap.dedent("""\
    Thank you for starting your search on Nextlanding!

    You'll receive an e-mail update when we're done (not more than 24 hours from now).

    If you have any questions or concerns, please reply to this e-mail.

    Thanks, and good luck on your apartment hunt!

    John, Gene, and Scott @ Nextlanding\
""")

CLIENT_RESULTS_SUBJECT_TEMPLATE = "Nextlanding: Your Apartment Search Results"

CLIENT_RESULTS_BODY_TEMPLATE = textwrap.dedent("""Hi,

You can see your list of apartments with verified availability information at: http://www.nextlanding.com/results/{0}

The full list of apartments are on the left, and the ones that are verified have a "verified" tab on the listing. If you click on a listing, you will be able to see the description and, if available, the verification data.

We will be updating the listings as we get more verification information so be sure to check back often.

You will always be able to access your search results from http://www.nextlanding.com/results/{0}. Thanks for using Nextlanding and we hope your apartment search is successful!

Best,

Gene @ Nextlanding

PS: We are still beta testing our service and we appreciate any feedback you have on how we did!
""")
