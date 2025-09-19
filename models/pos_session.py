from odoo import models, fields, api

class PosSession(models.Model):
    _inherit = 'pos.session'

    def action_change_owner(self):
        for session in self:
            session.user_id = 1   # Assign user with ID=1
        return True

    has_multiple_open_sessions = fields.Boolean(
        string="Has Multiple Open Sessions",
        compute="_compute_has_multiple_open_sessions"
    )

    @api.depends('user_id', 'state')
    def _compute_has_multiple_open_sessions(self):
        for session in self:
            if not session.user_id:
                session.has_multiple_open_sessions = False
                continue

            open_sessions = self.search_count([
                ('user_id', '=', session.user_id.id),
                ('state', '=', 'opened')
            ])
            session.has_multiple_open_sessions = open_sessions > 1
