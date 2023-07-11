# Apache Image
- httpd:2.4
- document root = /usr/local/apache2/htdocs/

# Azure Blob image rendering test
- index.html
```
hello world

<img src="https://<STG_NAME>.blob.core.windows.net/image/sample.png">

# SAS Token (Blob access level -> Private) 사용 시
# <URL>?<SASTOKEN> 
```