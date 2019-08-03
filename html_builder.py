def build(plants):
    html = ""

    with open('mail_start.html', 'r') as f:
        html += f.read()
    
    for p in plants:
        if p==1:
            with open('wet_plant.html', 'r') as f:
                html += f.read()
        else:
            with open('dry_plant.html', 'r') as f:
                html += f.read()
        print(p)
    
    with open('mail_end.html', 'r') as f:
        html += f.read()
    return html