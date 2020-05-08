# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "ESB :: Custom addons",
    "summary": "Custom addons for only esb project",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "author": "Ecosoft Co., Ltd",
    "license": "AGPL-3",
    "website": "https://ecosoft.co.th",
    "depends": ["hr", "mrp", "purchase"],
    "data": [
        "department/views/mrp_production_views.xml",
        "department/views/purchase_views.xml",
        "department/views/stock_scrap_views.xml",
        "mrp/views/mrp_production_views.xml",
        "product/views/product_views.xml",
        "purchase/views/purchase_views.xml",
    ],
    "installable": True,
}
