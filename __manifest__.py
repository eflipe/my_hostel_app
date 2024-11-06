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
        "data/data.xml",    
        "views/hostel_views.xml",    
        "views/hostel_room.xml",    
        "views/hostel_student.xml",    
        "views/hostel_amenities.xml",    
    ],
    # 'demo': [
    #     'demo.xml'
    # ],
    "installable": True,
}