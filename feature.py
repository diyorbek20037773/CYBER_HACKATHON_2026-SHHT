"""
Phishing URL Feature Extractor (30 features)
Adapted from ArnabKumarRoy02/Phishing-URL-Detection — bug fixes applied.
"""

import ipaddress
import re
import socket
from datetime import date
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

try:
    import whois
except Exception:
    whois = None


class FeatureExtraction:
    def __init__(self, url):
        self.features = []
        self.url = url
        self.domain = ""
        self.whois_response = None
        self.urlparse = None
        self.response = None
        self.soup = None

        try:
            self.response = requests.get(url, timeout=8, allow_redirects=True,
                                         headers={"User-Agent": "Mozilla/5.0"})
            self.soup = BeautifulSoup(self.response.text, "html.parser")
        except Exception:
            pass

        try:
            self.urlparse = urlparse(url)
            self.domain = self.urlparse.netloc
        except Exception:
            pass

        if whois is not None:
            try:
                self.whois_response = whois.whois(self.domain)
            except Exception:
                pass

        self.features = [
            self.UsingIp(),
            self.longUrl(),
            self.shortUrl(),
            self.symbol(),
            self.redirecting(),
            self.prefixSuffix(),
            self.SubDomains(),
            self.Hppts(),
            self.DomainRegLen(),
            self.Favicon(),
            self.NonStdPort(),
            self.HTTPSDomainURL(),
            self.RequestURL(),
            self.AnchorURL(),
            self.LinksInScriptTags(),
            self.ServerFormHandler(),
            self.InfoEmail(),
            self.AbnormalURL(),
            self.WebsiteForwarding(),
            self.StatusBarCust(),
            self.DisableRightClick(),
            self.UsingPopupWindow(),
            self.IframeRedirection(),
            self.AgeofDomain(),
            self.DNSRecording(),
            self.WebsiteTraffic(),
            self.PageRank(),
            self.GoogleIndex(),
            self.LinksPointingToPage(),
            self.StatsReport(),
        ]

    # 1. UsingIP
    def UsingIp(self):
        try:
            ipaddress.ip_address(self.domain.split(":")[0])
            return -1
        except Exception:
            return 1

    # 2. longUrl
    def longUrl(self):
        if len(self.url) < 54:
            return 1
        if 54 <= len(self.url) <= 75:
            return 0
        return -1

    # 3. shortUrl
    def shortUrl(self):
        pattern = (r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                   r'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                   r'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                   r'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|lnkd\.in|db\.tt|'
                   r'qr\.ae|adf\.ly|bitly\.com|cur\.lv|ity\.im|q\.gs|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|'
                   r'buzurl\.com|cutt\.us|u\.bb|yourls\.org|prettylinkpro\.com|scrnch\.me|filoops\.info|'
                   r'vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|link\.zip\.net')
        return -1 if re.search(pattern, self.url) else 1

    # 4. Symbol@
    def symbol(self):
        return -1 if "@" in self.url else 1

    # 5. Redirecting//
    def redirecting(self):
        return -1 if self.url.rfind('//') > 6 else 1

    # 6. prefixSuffix
    def prefixSuffix(self):
        try:
            return -1 if '-' in self.domain else 1
        except Exception:
            return -1

    # 7. SubDomains
    def SubDomains(self):
        dot_count = self.url.count('.')
        if dot_count == 1:
            return 1
        if dot_count == 2:
            return 0
        return -1

    # 8. HTTPS
    def Hppts(self):
        try:
            return 1 if self.urlparse and 'https' in self.urlparse.scheme else -1
        except Exception:
            return 1

    # 9. DomainRegLen
    def DomainRegLen(self):
        try:
            exp = self.whois_response.expiration_date
            cre = self.whois_response.creation_date
            if isinstance(exp, list):
                exp = exp[0]
            if isinstance(cre, list):
                cre = cre[0]
            age = (exp.year - cre.year) * 12 + (exp.month - cre.month)
            return 1 if age >= 12 else -1
        except Exception:
            return -1

    # 10. Favicon
    def Favicon(self):
        try:
            for link in self.soup.find_all('link', href=True):
                href = link['href']
                dots = [m.start() for m in re.finditer(r'\.', href)]
                if self.url in href or len(dots) == 1 or self.domain in href:
                    return 1
            return -1
        except Exception:
            return -1

    # 11. NonStdPort
    def NonStdPort(self):
        try:
            return -1 if len(self.domain.split(":")) > 1 else 1
        except Exception:
            return -1

    # 12. HTTPSDomainURL
    def HTTPSDomainURL(self):
        try:
            return -1 if 'https' in self.domain else 1
        except Exception:
            return -1

    # 13. RequestURL
    def RequestURL(self):
        try:
            i, success = 0, 0
            for tag in ('img', 'audio', 'embed', 'iframe'):
                for el in self.soup.find_all(tag, src=True):
                    src = el['src']
                    dots = [m.start() for m in re.finditer(r'\.', src)]
                    if self.url in src or self.domain in src or len(dots) == 1:
                        success += 1
                    i += 1
            if i == 0:
                return 0
            pct = success / i * 100
            if pct < 22.0:
                return 1
            if pct < 61.0:
                return 0
            return -1
        except Exception:
            return -1

    # 14. AnchorURL
    def AnchorURL(self):
        try:
            i, unsafe = 0, 0
            for a in self.soup.find_all('a', href=True):
                href = a['href']
                if "#" in href or "javascript" in href.lower() or "mailto" in href.lower() \
                        or not (self.url in href or self.domain in href):
                    unsafe += 1
                i += 1
            if i == 0:
                return -1
            pct = unsafe / i * 100
            if pct < 31.0:
                return 1
            if pct < 67.0:
                return 0
            return -1
        except Exception:
            return -1

    # 15. LinksInScriptTags
    def LinksInScriptTags(self):
        try:
            i, success = 0, 0
            for link in self.soup.find_all('link', href=True):
                href = link['href']
                dots = [m.start() for m in re.finditer(r'\.', href)]
                if self.url in href or self.domain in href or len(dots) == 1:
                    success += 1
                i += 1
            for script in self.soup.find_all('script', src=True):
                src = script['src']
                dots = [m.start() for m in re.finditer(r'\.', src)]
                if self.url in src or self.domain in src or len(dots) == 1:
                    success += 1
                i += 1
            if i == 0:
                return 0
            pct = success / i * 100
            if pct < 17.0:
                return 1
            if pct < 81.0:
                return 0
            return -1
        except Exception:
            return -1

    # 16. ServerFormHandler
    def ServerFormHandler(self):
        try:
            forms = self.soup.find_all('form', action=True)
            if not forms:
                return 1
            for form in forms:
                action = form['action']
                if action == "" or action == "about:blank":
                    return -1
                if self.url not in action and self.domain not in action:
                    return 0
            return 1
        except Exception:
            return -1

    # 17. InfoEmail
    def InfoEmail(self):
        try:
            text = str(self.soup)
            return -1 if re.findall(r"mail\(\)|mailto:", text) else 1
        except Exception:
            return -1

    # 18. AbnormalURL
    def AbnormalURL(self):
        try:
            return 1 if self.response.text == str(self.whois_response) else -1
        except Exception:
            return -1

    # 19. WebsiteForwarding
    def WebsiteForwarding(self):
        try:
            n = len(self.response.history)
            if n <= 1:
                return 1
            if n <= 4:
                return 0
            return -1
        except Exception:
            return -1

    # 20. StatusBarCust
    def StatusBarCust(self):
        try:
            return 1 if re.findall(r"<script>.+onmouseover.+</script>", self.response.text) else -1
        except Exception:
            return -1

    # 21. DisableRightClick
    def DisableRightClick(self):
        try:
            return 1 if re.findall(r"event\.button ?== ?2", self.response.text) else -1
        except Exception:
            return -1

    # 22. UsingPopupWindow
    def UsingPopupWindow(self):
        try:
            return 1 if re.findall(r"alert\(", self.response.text) else -1
        except Exception:
            return -1

    # 23. IframeRedirection
    def IframeRedirection(self):
        try:
            return 1 if re.findall(r"<iframe>|<frameBorder>", self.response.text) else -1
        except Exception:
            return -1

    # 24. AgeofDomain
    def AgeofDomain(self):
        try:
            cre = self.whois_response.creation_date
            if isinstance(cre, list):
                cre = cre[0]
            today = date.today()
            age = (today.year - cre.year) * 12 + (today.month - cre.month)
            return 1 if age >= 6 else -1
        except Exception:
            return -1

    # 25. DNSRecording
    def DNSRecording(self):
        try:
            cre = self.whois_response.creation_date
            if isinstance(cre, list):
                cre = cre[0]
            today = date.today()
            age = (today.year - cre.year) * 12 + (today.month - cre.month)
            return 1 if age >= 6 else -1
        except Exception:
            return -1

    # 26. WebsiteTraffic — alexa retired; degrade gracefully
    def WebsiteTraffic(self):
        return -1

    # 27. PageRank
    def PageRank(self):
        try:
            r = requests.post("https://www.checkpagerank.net/index.php",
                              data={"name": self.domain}, timeout=5)
            m = re.findall(r"Global Rank: ([0-9]+)", r.text)
            if m:
                rank = int(m[0])
                if 0 < rank < 100000:
                    return 1
            return -1
        except Exception:
            return -1

    # 28. GoogleIndex
    def GoogleIndex(self):
        # googlesearch ko'p hollarda CAPTCHA — neutral default
        return 1

    # 29. LinksPointingToPage
    def LinksPointingToPage(self):
        try:
            n = len(re.findall(r"<a href=", self.response.text))
            if n == 0:
                return 1
            if n <= 2:
                return 0
            return -1
        except Exception:
            return -1

    # 30. StatsReport
    def StatsReport(self):
        try:
            url_match = re.search(
                r'at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|'
                r'myjino\.ru|96\.lt|ow\.ly', self.url)
            ip_address = socket.gethostbyname(self.domain.split(":")[0])
            ip_match = re.search(
                r'146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|'
                r'78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|'
                r'83\.125\.22\.219|46\.242\.145\.98|107\.151\.148\.44|107\.151\.148\.107|'
                r'64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|'
                r'119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|'
                r'118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|'
                r'175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|'
                r'103\.232\.215\.140|69\.172\.201\.153|216\.218\.185\.162|54\.225\.104\.146|'
                r'103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|'
                r'62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|'
                r'34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|'
                r'192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|'
                r'52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|216\.38\.62\.18|'
                r'104\.130\.124\.96|47\.89\.58\.141|54\.86\.225\.156|54\.82\.156\.19|'
                r'37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42', ip_address)
            if url_match or ip_match:
                return -1
            return 1
        except Exception:
            return 1

    def getFeaturesList(self):
        return self.features
