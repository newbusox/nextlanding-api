import textwrap

CLIENT_RESULTS_SUBJECT_TEMPLATE = "Nextlanding: Your Apartment Search Results"

CLIENT_RESULTS_BODY_TEMPLATE = textwrap.dedent("""Hi,

You can see your list of apartments with verified availability information at: \
http://www.nextlanding.com/results/{0}

The full list of apartments are on the left, and the ones that are verified have a "verified" tab on the listing.\
 If you click on a listing, you will be able to see the description and, if available, the verification data.

We will be updating the listings as we get more verification information so be sure to check back often.

You will always be able to access your search results from http://www.nextlanding.com/results/{0}. \
Thanks for using Nextlanding and we hope your apartment search is successful!

Best,

Gene @ Nextlanding

PS: We are still beta testing our service and we appreciate any feedback you have on how we did!
""")
