import re
from typing import Optional


def gs_url_to_key(gs_url: str) -> Optional[str]:
    match = re.match(r"gs://[^/]+/(.+)", gs_url)
    if match:
        return match.group(1)
    return None