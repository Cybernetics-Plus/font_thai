# -*- coding: utf-8 -*-
from odoo import fields, models

class ResCompany(models.Model):
    "Add Fonts Thai to Document Layout."
    _inherit = "res.company"

    font = fields.Selection(
        selection_add=[
            ("AngsanaNew", "AngsanaNew"),
            ("BaiJamjuree", "BaiJamjuree"),
            ("ChakraPetch", "ChakraPetch"),
            ("Fahkwang", "Fahkwang"),
            ("IBMPlexSansThai", "IBMPlexSansThai"),
            ("Kanit", "Kanit"),
            ("Kodchasan", "Kodchasan"),
            ("Maitree", "Maitree"),
            ("Mitr", "Mitr"),
            ("Niramit", "Niramit"),
            ("NotoSerifThai", "NotoSerifThai"),
            ("Pridi", "Pridi"),
            ("Prompt", "Prompt"),
            ("Sarabun", "Sarabun"),
            ("Taviraj", "Taviraj"),
            ("Trirong", "Trirong"),
            ("THSrisakdi", "THSrisakdi"),
            ("THSarabunNew", "THSarabunNew"),
            ("THSarabun", "THSarabun"),
            ("THNiramitAS", "THNiramitAS"),
            ("THMaliGrade6", "THMaliGrade6"),
            ("THKrub", "THKrub"),
            ("THKoHo", "THKoHo"),
            ("THKodchasal", "THKodchasal"),
            ("THK2DJuly8", "THK2DJuly8"),
            ("THFahkwang", "THFahkwang"),
            ("THCharmonman", "THCharmonman"),
            ("THCharmofAU", "THCharmofAU"),
            ("THChakraPetch", "THChakraPetch"),
            ("THBaijam", "THBaijam"),
            ("Webdings", "Webdings"),
        ]
    )
