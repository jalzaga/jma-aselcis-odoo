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

import itertools
from lxml import etree

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.osv.orm import except_orm
from openerp.exceptions import Warning, RedirectWarning
import openerp.addons.decimal_precision as dp
from openerp.tools.float_utils import float_round as round


class res_partner(osv.osv):
    _inherit = "res.partner"
    
    _columns = {
        'picking_notes': fields.text('Picking Notes', help="Notes to be included in the picking list"),                       
    }

class sale_order(osv.osv):
    _inherit = "sale.order"
    
    def onchange_delivery_id(self, cr, uid, ids, company_id, partner_id, delivery_id, fiscal_position, context=None):
        result = super(sale_order, self).onchange_delivery_id(cr, uid, ids, company_id, partner_id, delivery_id, fiscal_position, context=context)
        if delivery_id <> partner_id:
            picking_notes = self.pool.get('res.partner').browse(cr, uid, delivery_id, context=context).picking_notes
            if picking_notes:
                result['value']['picking_notes'] = picking_notes
        else:
            picking_notes = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context).picking_notes
            result['value']['picking_notes'] = picking_notes or False
        return result
    
    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        result = super(sale_order, self).onchange_partner_id(cr, uid, ids, part, context=context)
        if part:
            picking_notes = self.pool.get('res.partner').browse(cr, uid, part, context=context).picking_notes
            result['value']['picking_notes'] = picking_notes or False
        return result
    
    _columns = {
        'picking_notes': fields.text('Picking Notes', help="Notes to be included in the picking list"),           
    }

class stock_picking(osv.osv):
    _inherit = "stock.picking"
    
    def create(self, cr, user, vals, context=None):
        if vals:
            sale_obj = self.pool.get('sale.order')
            sale_ids = sale_obj.search(cr, user, [('name', '=', vals['origin'])], context=context)
            picking_notes = sale_obj.browse(cr, user, sale_ids, context=context).picking_notes
            if picking_notes:
                vals['picking_notes'] = picking_notes
        return super(stock_picking, self).create(cr, user, vals, context=context)

    
    _columns = {
        'picking_notes': fields.text('Picking Notes', help="Notes to be included in the picking list"),           
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
