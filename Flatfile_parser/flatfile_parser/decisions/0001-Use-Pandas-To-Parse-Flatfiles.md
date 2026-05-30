## Context

The task was to find the lightweight flatfile parser

## Considered Options

* pandas
* flatfile
* flatfile-mapping

## Decision Outcome

Chosen option: pandas since its a reliable and well-known solution to work with various data formats. `flatfile` offers many more functions if it comes to handling flatfiles which wouldn't be needed. `flatfile-mapping` seems like the least-developed project from these three.