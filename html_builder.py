def build(plants):
    html = ""

    with open('./html/mail_start.html', 'r') as f:
        html += f.read()
    
    for p in plants:
        if p==1:
            with open('./html/wet_plant.html', 'r') as f:
                html += f.read()
        else:
            with open('./html/dry_plant.html', 'r') as f:
                html += f.read()
    
    with open('./html/mail_end.html', 'r') as f:
        html += f.read()
    return html