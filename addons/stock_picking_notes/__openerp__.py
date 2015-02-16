# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2015 Aselcis Consulting (<http://www.aselcis.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'stock_picking_notes',
    'version' : '1.1',
    'author' : 'Jose Maria Alzaga - Aselcis Consulting',
    'category' : 'Sales & Stock',
    'description' : """
Stock Picking Notes
===================

Features covered
----------------
    * Adds internal picking notes to customer
    * Internal picking notes go to the sales order when the customer is selected, 
      they go to the picking when the order is confirmed. 
      They can be modified in the sales order and in the picking.



    """,
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['base_setup', 'sale','stock' ],
    'data': [
       'res_partner_view.xml',
       'sale_view.xml',
       'stock_view.xml',
    ],


    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
