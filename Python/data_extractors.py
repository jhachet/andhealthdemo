from datetime import datetime

def get_value(d, keys, default=None):
    for key in keys:
        d = d.get(key, {})
        if not isinstance(d, (dict, list)):
            break
    return d if isinstance(d, (str, int, bool)) else default

def count_items(d, key):
    items = d.get(key, [])
    return len(items) if isinstance(items, list) else 0


def extract_snapshot(data, snapshot_date):
    extracted_data = []
    for entity in data.get('coveredEntities', []):
        extracted_data.append({
            "snapshotDate": snapshot_date,
            "ceId": entity.get("ceId"),
            "name": entity.get("name"),
            "subName": entity.get("subName"),
            "participating": entity.get("participating"),
            "isParticipating": 1 if entity.get("participating") == "TRUE" else 0,
            "grantNumber": entity.get("grantNumber"),
            "terminationReason": entity.get("terminationReason"),
            "numShippingAddresses": count_items(entity, "shippingAddresses"),
            "numMedicaidNumbers": count_items(entity, "medicaidNumbers"),
            "numContractPharmacies": count_items(entity, "contractPharmacies"),
            "participatingStartDate": entity.get("participatingStartDate"),
            "terminationDate": entity.get("terminationDate"),
        })
    return extracted_data

def extract_dim_covered_entity(data, snapshot_date):
    extracted_data = []
    for entity in data.get('coveredEntities', []):
        extracted_data.append({
            "id340B": entity.get("id340B"),
            "ceId": entity.get("ceId"),
            "entityType": entity.get("entityType"),
            "name": entity.get("name"),
            "participating": entity.get("participating"),
            "participatingStartDate": entity.get("participatingStartDate"),
            "medicareProviderNumber": entity.get("medicareProviderNumber"),
            "streetAddress.addressLine1": get_value(entity, ["streetAddress", "addressLine1"]),
            "streetAddress.city": get_value(entity, ["streetAddress", "city"]),
            "streetAddress.state": get_value(entity, ["streetAddress", "state"]),
            "streetAddress.zip": get_value(entity, ["streetAddress", "zip"]),
            "billingAddress.addressLine1": get_value(entity, ["billingAddress", "addressLine1"]),
            "billingAddress.city": get_value(entity, ["billingAddress", "city"]),
            "billingAddress.state": get_value(entity, ["billingAddress", "state"]),
            "billingAddress.zip": get_value(entity, ["billingAddress", "zip"]),
            "rural": entity.get("rural"),
        })
    return extracted_data

def extract_fact_contract_pharmacies(data, snapshot_date):
    extracted_data = []
    for entity in data.get('coveredEntities', []):
        for pharmacy in entity.get("contractPharmacies", []):
            extracted_data.append({
                "snapshotDate": snapshot_date,
                "ceId": entity.get("ceId"),
                "contractPharmacyName": pharmacy.get("name"),
                "contractId": pharmacy.get("contractId"),
                "pharmacyId": pharmacy.get("pharmacyId"),
                "beginDate": pharmacy.get("beginDate"),
                "terminationDate": pharmacy.get("terminationDate"),
                "address.addressLine1": get_value(pharmacy, ["address", "addressLine1"]),
                "address.city": get_value(pharmacy, ["address", "city"]),
                "address.state": get_value(pharmacy, ["address", "state"]),
                "address.zip": get_value(pharmacy, ["address", "zip"]),
                "phoneNumber": pharmacy.get("phoneNumber"),
            })
    return extracted_data