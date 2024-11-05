{
    "name": "Hostel Management",  # Module title
    "summary": "Manage Hostel easily",  # Module subtitle phrase
    "description": "Efficiently manage the entire residential facility in the school.",  # Supports reStructuredText(RST) format (description is Deprecated)
    "version": "17.0.1.0.0",
    "author": "LOL producciones",
    "category": "Tools",
    "website": "http://www.example.com",
    "license": "",
    "depends": ["base"],

    'data': [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel_views.xml",    
    ],
    # 'demo': [
    #     'demo.xml'
    # ],
    "installable": True,
}