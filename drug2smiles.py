import requests


def get_smiles_from_compound_name(compound_name):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/property/CanonicalSMILES/JSON"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        smiles = (
            data.get("PropertyTable", {})
            .get("Properties", [{}])[0]
            .get("CanonicalSMILES")
        )
        return smiles
    except requests.RequestException as e:
        print(f"Error retrieving SMILES for compound name {compound_name}: {e}")
        return None
