# Newsletter Scraper

This program is meant to scrap the values needed for the table of the newsletter published by [Stratefi203](http://www.stratefi203.com/). This module is still an early developer preview. Features and implementation are subject to change.

The desired output is a PNG [file](https://github.com/Arthurim/Stratefi203/blob/master/pictures/Table.png).

## Getting Started

You need to have the following two CSV files in order to run this program:
The first one, [ComputingTable](https://github.com/Arthurim/Stratefi203/blob/master/pictures/ComputingTable.JPG) is used to perform the computation.

The second one, [ValuesTable](https://github.com/Arthurim/Stratefi203/blob/master/pictures/ValuesTable.JPG) is the table in which the desired outputs are saved and from which the PNG file is created.

## Methodology

The program is divided in two parts
- the scraping part
- the graphing part

### Scraping
scraper.py

The scraper function scraps the value for a given ticker and asset class.
The *clean* fucntion
### Graphing
graph.py

## Future work

- Scraping the upcoming events
- Selecting the news articles
- Summurazing news articles
- Writing the email automatically