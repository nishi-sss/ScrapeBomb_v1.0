def scrape_jobs():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    URL = "https://xn--pckua2a7gp15o89zb.com/岡山県岡山市での仕事"
    EXCLUDE_KEYWORDS = ['人材', '派遣']
    results = []

    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, 'html.parser')

    job_titles = soup.find_all("span", class_="p-result_name")

    for job in job_titles:
        title = job.get_text(strip=True)
        if any(keyword in title for keyword in EXCLUDE_KEYWORDS):
            continue
        results.append({"職種名": title})

    df = pd.DataFrame(results)
    return df

