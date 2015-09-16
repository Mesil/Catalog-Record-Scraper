# Catalog-Record-Scraper
This is a simple webscraper for extracting information from digital catalogs based on the presence of keywords.
This tool is based on the Scrapy framework and, as such, requires the presence and use of scrapy to run. Instructions on installing scrapy may be found here: http://doc.scrapy.org/en/latest/intro/install.html. Once Scrapy in installed, this tool can be used by opening the terminal, moving to the directory containing the project files, and entering the comand 'scrapy crawl catalog'. If the program is working correctly, it should generate a .csv file whose contents match those of 'testscrape.csv'.
As is, this tool is of extreemly narrow use. Happily, modifying the tool is a straightforward—if not easy—task.
The first file to addapt is 'items.py' located in the 'Catalog_Scraper' subdirectory; there you can define the information you wish to retrieve from catalog records. To produce a simple test case, only the 'title' item is curently active, but new items can be defined following the format provided by 'title' and the other items which are currently commented out.
Once the you have determined the information you wish to retrieve, the next step is to apply those items to the .csv file which the tool generates. That is acomplished by modifying the 'pipelines.py' file, also contained in the 'Catalog_Scraper' subdirectory. By declairing the items defined in 'items.py' as fields to export in line 28 of 'pipelines.py'you can identify them for inclusion in the .csv file generated, as well as specify the order in which they appear. The location of the pipeline you create must also be specified in the 'settings.py' file located in the 'Catalog_Scraper' subdirectory.
With the information you wish to retrieve identified and slated for inclusion in the resulting .csv, you must define the method for gathering it. That procedure is specified in the file 'catalogscraper.py'. In line 13, alowed domains can be specified to limit the crawl by ensueing that is only searches pages within the specified domain. The 'start_urls' in line 14 tell the tool where to begin its search of the catalog. Line 17 allows you to indicate where the tool should look to retrieve information by providing a piece of hyperlink common to catalog records. The 'callback', also in line 17, directs the tool where to pass the links identified as allowed. With the name of the method provided in 'callback', its definition tells the tool how to extract information from the links identified as allowed. In line 30, you can see how information is identified; the category of information is identified first, followed by a path to its location. In the example, that locating information is identified as an xpath. Finally, the 'catalogscraper.py' file also impliments a keyword search. In line 26, the file 'keys.txt' is opened and its contents combined into a regular expression with each word seperated by the charater '|', the symbol for the logical operator 'or'. In line 27, the regular expression defined in line 26 is saved for reuse and the tool instructed to ignore the case of keywords it contains. At the begining of the content extraction in line 28, an if condition is implimented, instructing the tool to only extract the content of catalog records containging one of the keywords.
The 'keys.txt' file, located in the 'spiders' subdirectory, is responsible for the keyword searches performed in the parse_CatalogRecord. Each of the keywords whose presence you require is simply listed in 'keys.txt' on its own line. In future, I hope to provide a range of files with related search methods that will support more complex keyword searches, such as only accepting a keyword when another keyword is also present.
