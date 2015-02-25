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
from openerp.tools.translate import _
from openerp.osv import fields, osv
from openerp.osv.orm import except_orm
from openerp.exceptions import Warning, RedirectWarning
from openerp.tools.float_utils import float_round as round



class res_partner(osv.osv):
    _inherit = "res.partner"
    
    def _check_unique_vat(self, cr, uid, ids,vat, is_company, context=None):
        vals=[]
        vals = self.search(cr,  uid, [('vat','=',vat),('is_company','=',True)], context=context)
        return len(vals)

    def onchange_vat(self, cr, uid,ids,vat,is_company,context=None):
        dups=self._check_unique_vat(cr,uid,ids,vat,is_company,context=context)
        if dups != 0:
            return {'warning': {'title': _('warning'),
                                'message':  _('The VAT code already exists in the database'),
                                },
                    }
        return True            
                
            


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
