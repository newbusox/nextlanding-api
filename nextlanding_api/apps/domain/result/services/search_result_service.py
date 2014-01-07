from nextlanding_api.apps.domain.apartment.services.apartment_amenity_service import get_amenities_dict
from nextlanding_api.apps.domain.result.models import SearchResult


def get_results_from_search(search):
  return (
    SearchResult
    .objects
    .filter(search_aggregate_id=search.pk)
    .extra(select=
    {
      'has_availability': '''
                          CASE WHEN availability_last_response_date is NOT NULL
                          THEN 1
                          ELSE -1
                          END
                          '''
    })
    .order_by('-has_availability', '-availability_last_response_date')
  )


def get_result_from_aggregate(result):
  return SearchResult.objects.get(result_aggregate_id=result.pk)


def save_or_update(result):
  result.save(internal=True)


def create_search_result(result_aggregate):
  apartment = result_aggregate.apartment
  listing_urls = [l.url for l in apartment.listings.exclude(is_deleted=True)]
  latest_listing = apartment.listings.order_by("-last_updated_date")[:1].get()

  result = SearchResult(
    result_aggregate_id=result_aggregate.pk,
    apartment_aggregate_id=result_aggregate.apartment_id,
    search_aggregate_id=result_aggregate.search_id,
    address=apartment.address,
    lat=apartment.lat,
    lng=apartment.lng,
    broker_fee=apartment.broker_fee,
    price=apartment.price,
    bedroom_count=apartment.bedroom_count or 0,
    bathroom_count=apartment.bathroom_count or 1,
    sqfeet=apartment.sqfeet,
    listing_urls=listing_urls,
    last_updated_date=latest_listing.last_updated_date or latest_listing.posted_date,
    description=latest_listing.description,
    contact_name=latest_listing.contact_name,
    contact_phone_number=latest_listing.contact_phone_number,
    contact_email_address=latest_listing.contact_email_address,
    amenities=get_amenities_dict(apartment),
    compliance_score=result_aggregate.compliance_score,
    availability_contact_response=result_aggregate.availability_contact_response,
    availability_last_response_date=result_aggregate.availability_last_response_date,
    availability_system_name=result_aggregate.availability_type.system_name
  )

  save_or_update(result)

  return result


def update_availability_response(result):
  search_result = get_result_from_aggregate(result)
  search_result.availability_contact_response = result.availability_contact_response
  search_result.availability_last_response_date = result.availability_last_response_date
  search_result.availability_system_name = result.availability_type.system_name

  save_or_update(search_result)
