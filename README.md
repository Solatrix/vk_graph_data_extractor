# VK Graph Data Extractor
### The Idea
Extracting information from social media can be quite the hassle. Whilst crawlers do exist for a comprehensive amount of social media (Facebook, Twitter, Instagram, TikTok) community extractions is a different task.
This scraper aims at extracting data from VKontakte communities to look for link with other communities. In essence it outputs graphs where each node is a community and each link is a hyperlink referenced from one page community page to the other.

### The algorithm

This scraper is intended for research purposes. 
This algorithm was developed using Python 3.8 and lacks consistent typing.

Using the Selenium web driver each VKontakte community page is rendered and crawled using an HTML selector.
Links found in these selectors are added to the nodes table as newly found communities. Links are created in the links table between the page in which they were found and the newly found community.

Use example : 
```Python
import Scraper

VKScraper = Scraper({
	'source':'sites.txt',
	'threading' : True,
	'AllowJS' : True,
	'hyperlinks_selector' : ["aside div#public_links a[href]","div#group_links a[href]"],
	'other_data' : ["span.header_count"],
	'output' : {
		'type' : 'graph',
		'nodes' : ['id','uri','group_members']
	}
})
```
#### Minimal settings to use the library
```Python
import Scraper

Scraper ({
  # Your input file required
  'source':'source.txt',
  # The output format, for now graph is the only option and outputs a nodes.csv and a links.csv file
  'output':{
    'type':'graph',
    'nodes':['column', 'column','column'] # Name of the columns you wish to see in output, by default Id is present for each individual node
  },
  # Much necessary for modern webpages rendering, uses a Javascript rendering engine
  'AllowJS' : True
})

```
The `source` argument is essentialy a text file where each line is a HTTPS link to a VK community.
```text
https://vk.com/myCommunityAddress
https://vk.com/myOhterCommunityAddress
https://vk.com/myThirdCommunityAddress
```
The `AlloWJS` argument is necessary for rendering pages with JS content, especially on Social Media where AJAX loading is virtually everywhere.

The `threading` argument is optionally left to ```True ``` and allows for simultaneous pages lookup.

The `hyperLinksSelector` argument is a CSS selector which is looking for HTML elements consisting of other links to VK communities. In this example we're using the "Links" section in the right bottom hand corner of VK community pages.

The `other_data` is a List consisting of CSS Selectors which you can use to scrap other data about a community. In the example above, I'm using it to extract member counts.
 
 
### And then

Both `nodes.csv` and `links.csv` files can be used in graph rendering software on Desktop and online solutions. Data is to be further analyzed and reprojected using Gephi or D3js as force-directed graph. Depending on the columns you've extracted, the data can be processed using ETLs, or statistical analysis with Pandas


### Issues
The algorithm does not support recursitivity which would enable for deeper community lookup. The scripts would benefit from a in-depth refactoring using Python 3.10 strong typing :)
If you're encountering issues whilst using the library, feel free to open an issue.

~Disclaimer~ : There are numerous security vulnerability in `requirements.txt` packages, using this library on an industrial platform is strongly discouraged
