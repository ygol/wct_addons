# -*- encoding: utf-8 -*-

{
    "name" : "Comptabilité - Tunisie",
    "version" : "1.0",
    "author" : "WHITECAPETECH : Sami RJIBA",
    "website": "http://www.whitecapetech.com",
    "category" : "Localization/Account Charts",
    "description": """
Ce le module permet de gérer le plan comptable Tunisien en Odoo. 
================================================================

Ce Module charge le modèle du plan de comptes standard Tunisien et permet de
générer les états comptables aux normes tunisiennes (Bilan, CPC (comptes de
produits et charges), balance générale à 6 colonnes, Grand livre cumulatif...).
L'intégration comptable a été validé avec l'aide du Cabinet d'expertise comptable.""",

    "depends" : ['base','account'],
    "init_xml" : [],
    "data" : [
        'plan_comptable_general.xml',
        'tn_pcg_taxes.xml',
        'tn_tax.xml',
		'l10n_tn_wizard.xml',
        'security/ir.model.access.csv',
		     ],
    "test": [],
    "demo_xml" : [],
    "active": True,
    "installable": True,
	'images': ['images/config_chart_l10n_tn.jpg', 'images/l10n_tn_chart.jpg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
