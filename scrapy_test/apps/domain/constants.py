import textwrap

POTENTIAL_SEARCH_SESSION_ID = 'potential_search_session_id'

EMAILER_SENDER_SUBJECT_TEMPLATE = "{{ address }} Apartment"
EMAILER_SENDER_BODY_TEMPLATE = textwrap.dedent("""\
    Hi{% if apartment.contact_first_name %} {{ apartment.contact_first_name }}{% endif %},

    I saw your listing on {{ source }} for an apartment at {{ apartment.address1 }} ({% if apartment.bedroom %}{{ apartment.bedroom|floatformat }} BR{% else %}studio{% endif %} for ${{ apartment.price|floatformat:"-2" }}). I'm interested in this apartment. Is it still available? If so, when can I see it? Can you tell me anything else about the place?

    Thanks,
    {{ signature }}\
""")
