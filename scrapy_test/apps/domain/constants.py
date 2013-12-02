import textwrap

POTENTIAL_SEARCH_SESSION_ID = 'potential_search_session_id'

EMAILER_SENDER_SUBJECT_TEMPLATE = "{{ address }} Apartment"
EMAILER_SENDER_BODY_TEMPLATE = textwrap.dedent("""\
    Hi{% if contact_name %} {{ contact_name }}{% endif %},

    I saw your listing on {{ source }} for an apartment at {{ address }} ({% if bedroom %}{{ bedroom|floatformat }} BR{% else %}studio{% endif %} for ${{ price|floatformat:"-2" }}). I'm interested in this apartment. Is it still available? If so, when can I see it? Can you tell me anything else about the place?

    Thanks,
    {{ from_name }}\
""")
