# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 2014  Renato Lima - Akretion                                  #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from openerp import models, api


class ProcurementOrder(models.Model):
    _inherit = "procurement.order"

    @api.model
    def _run_move_create(self, procurement):
        result = super(ProcurementOrder, self)._run_move_create(procurement)
        if procurement.sale_line_id:
            result.update({
                'fiscal_category_id': (procurement
                                       .sale_line_id.fiscal_category_id.id),
                'fiscal_position': procurement.sale_line_id.fiscal_position.id,
            })
        return result
