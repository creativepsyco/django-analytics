django-analytics
================

A Generic Product Analytics Dashboard. Add new products and indicators without relying on Django Models or their definitions.

This is more of a automation and design-related application, so that data collection, aggregation and presentation is simplified, when developed fully, I hope to add custom data source integration and automatic presentation of the aggregated statistics.

###Assumptions
* Different Django apps for different products, the SQL relies on this.
* The analytics tables assume that the name begins with `[product]_[indicator_name]`. Later on this will not be needed when we will have pluggable data processors
* Also it needs the columns in those tables to be according to the ones in Indicator model. Again, this won't be needed when there will be internal data processors working 

###Targets for v0.1
In this I don't plan to integrate the data sources, i shall assume that the data sources exists and plan to have a concrete dependency on it. Removing this dependency shall be dealt later on.

This version hopes to support the following:

* Support simple aggregational analytics Sum, Min, Max etc.
* Admin interface for adding products and different types of analytics

###LICENSE

The MIT License (MIT)

Copyright (c) 2014 Mohit Kanwal

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
