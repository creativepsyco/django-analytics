django-analytics
================

A Generic Product Analytics Dashboard. Add new products and indicators without relying on Django Models or their definitions.

This is more of a automation and design-related application, so that data collection, aggregation and presentation is simplified, when developed fully, I hope to add custom data source integration and automatic presentation of the aggregated statistics.

###Assumptions
* Different Django apps for different products, the SQL relies on this.

###Targets for v0.1
In this I don't plan to integrate the data sources, i shall assume that the data sources exists and plan to have a concrete dependency on it. Removing this dependency shall be dealt later on.

This version hopes to support the following:

* Support simple aggregational analytics Sum, Min, Max etc.
* Admin interface for adding products and different types of analytics