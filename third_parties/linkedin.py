# required for to access environment variable
import os

# required for to make api call
import requests

# required for to load environment variables
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/mukeshyadav/b0be77bb47e4d4853cadc8fa14f5c8f9/raw/c370b196f59fe04726b7acdd1567400ba925f84f/eden-marco.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint="https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response=requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    data = response.json()
    data = {
        k: v
        for k,v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://linkedin.com/in/eden-marco/", mock=True)
    )

