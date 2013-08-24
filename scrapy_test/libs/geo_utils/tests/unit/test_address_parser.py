import pytest
from scrapy_test.libs.geo_utils.parsing import address_parser


@pytest.mark.parametrize(("input_values", "expected"), [
  ('123 fake st', True),
  ('100 e 55th', True),
  ('5th', False),
  ('5th and 55th', False),
])
def test_address_parser_detects_correct_street_addresses(input_values, expected):
  assert expected == address_parser.is_street_address(input_values)

@pytest.mark.parametrize(("input_values", "expected"), [
  ('62nd at york', True),
  ('21 and broadway', True),
  ('Macon st at Marcy ave', True),
  ('67 w 58th', False),
  ('250 e66', False),
])
def test_address_parser_detects_correct_cross_street_addresses(input_values, expected):
  assert expected == address_parser.is_cross_street_address(input_values)

@pytest.mark.parametrize(("input_values", "expected"), [
  ('123 fake st #99', '#99'),
  ('123 fake st', None),
  ('Some place ste 67', 'ste 67'),
  ('Some place apt. 55', 'apt. 55'),
])
def test_address_parser_detects_address2(input_values, expected):
  assert expected == address_parser.get_address2(input_values)

def test_address_parser_joins_cross_street():
  assert 'Foo & Bar' == address_parser.join_cross_street(('Foo','Bar'))
