import requests


def convert(url: str) -> str:
    if url.startswith("https://music.apple.com/"):
        dst = "spotify"
    elif url.startswith("https://open.spotify.com/"):
        dst = "appleMusic"
    else:
        raise ValueError("URL passed to convert method is invalid")

    rsp = requests.get(
        "https://api.song.link/v1-alpha.1/links",
        params={
            "url": url,
            "songIfSingle": "true",
        }
    )
    assert rsp.status_code == 200

    result = rsp.json()
    return result["linksByPlatform"][dst]["url"]
