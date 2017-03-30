### WebDefender
WebDefender enhances the anti-tracking technology originally developed by the Electronic Frontier Foundation for the browser extension Privacy Badger. Implemented natively within “Smart Protect - Web”, WebDefender uses machine learning to detect third-party websites who are exhibiting tracking behavior and blocks them.

#### UI Enablement (in SWE Browser):
 * Default: toggle the option in Menu > Settings > Site settings > "Web Defender"
 * Per-site (Overrides the default option on a per-website basis): toggle the option in Top-left Favicon Button > "Web Defender"

#### Configuration:
 - Web Defender is enabled by default.
 - Web Defender can use Disconnect.me's services.json list to improve the user experiencing by white-listing CDN domains that serve website contents which would otherwise be blocked by Web Defender and cause breakages in some websites.

 - To configure URL to your Disconnect.me services list
```
       {
          "version": "1.0",
          "update": {},
          "subscriptions": [
            {
              "name"            : "DisconnectMe Services List",
              "category"        : "DISCONNECT_ME_SERVICES_LIST",
              "format"          : "WebDefender 1.0",
              "url"             : "<url-to-services-list>",
              "expiration"      : "4 days"
            }
          ]
        }
```
    - Create a file called **web_defender_conf** with the above configuration
    - Add a valid URL in place of **<url-to-services-list>**
    - Copy the **web_defender_conf** into **<your-channel>/res/raw/web_defender_conf** and build your browser.

#### WebDefender libraries:
 - The libraries listed in this repository are built on top of SWE based on Chromium version specified in the VERSION file. Attempting to use these libraries in any other version of chromium will result in instability.
 - `libswewebrefiner.so` is built with dependency on `libswe.so`. If you are changing the chromium library name to something else in your project, then `libswewebrefiner.so` library loading will simply fail at runtime.
 - Libraries support ARM (32-bit) architecture only.

#### Browser command line arguments:
```
--disable-web-defender              disables WebDefender completely
--enable-web-refiner-logcat-stats   enables logcat output of WebDefender and WebRefiner actions
```

#### Debugging: Logcat messages:
```
logcat -s WebDefender       generic WebDefender failure messages
logcat -s WebDefenderStat   filter stats when '--enable-web-refiner-logcat-stats' is used
```
