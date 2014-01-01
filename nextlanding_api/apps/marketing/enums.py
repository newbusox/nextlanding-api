from nextlanding_api.libs.python_utils.types.enum import enum

ProductEnum = enum(
  Search=1,
)

ProductChoices = (
  (ProductEnum.Search, 'Search'),
)

DidNotRespondEnum = enum(
  AlreadyMessaged=1,
  MissingInformation=2,
  IgnoreRecipient=3,
)

DidNotRespondChoices = (
  (DidNotRespondEnum.AlreadyMessaged, 'Already Messaged Recipient'),
  (DidNotRespondEnum.MissingInformation, 'Missing Information'),
  (DidNotRespondEnum.IgnoreRecipient, 'Recipient Ignored'),
)
