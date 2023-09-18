# Read the category and the related resources from the tsv file
# generate a html from that

import pandas as pd
import math

# generate the start
def generate_start(language):
    if language == "en":
        start = """<!DOCTYPE html>\n<html>\n\n<head>\n\t<title>EPFL Sustainability Resources</title>\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n\t<link rel="icon" href="logo\Durabilite.png">\n</head>\n\n<body>\n\t<div class="container" id="intro">\n\t\t<div class="banner">\n\t\t\t<div class="title">\n\t\t\t\tEPFL Sustainability Resources\n\t\t\t</div>\n\t\t\t<div class="lang">\n\t\t\t\t<div class="dropdown toggle">\n\t\t\t\t\t<input id="t1" type="checkbox" unchecked>\n\t\t\t\t\t<label for="t1">language</label>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="index.html">English</a></li>\n\t\t\t\t\t\t<li><a href="index_fr.html">Francais</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="appetizer">\n\t\t\t<div class="text">\n\t\t\t\t<h1>Discover sustainability on your campus!</h>\n\t\t\t\t\t<p>There are many resources & staff available for students on EPFL campus regarding sustainability.\n\t\t\t\t\t\tThis website, built by students <i>(Mehdi El Bouari & Ke Li, 2023)</i>, aims to provide a\n\t\t\t\t\t\tcomprehensive\n\t\t\t\t\t\tlist of these resources, and to make them easily accessible to all.\n\t\t\t\t\t</p>\n\t\t\t\t\t<p>To get in touch with the sustainability education team about this site or for other reasons,\n\t\t\t\t\t\tdon’t\n\t\t\t\t\t\thesitate to contact <a href="mailto:sustainability@epfl.ch">sustainability@epfl.ch</a> for\n\t\t\t\t\t\tmore information!\n\t\t\t\t\t</p>\n\t\t\t</div>\n\t\t\t<div class="subbubble-container" id="subbubbles">\n\t\t\t\t<div class="midcontainer" id="upper_subbubbles">\n"""
    else:
        start = """<!DOCTYPE html>\n<html>\n\n<head>\n\t<title>EPFL Sustainability Resources</title>\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n\t<link rel="icon" href="logo\Durabilite.png">\n</head>\n\n<body>\n\t<div class="container" id="intro">\n\t\t<div class="banner">\n\t\t\t<div class="title">\n\t\t\t\tEPFL Ressources durables\n\t\t\t</div>\n\t\t\t<div class="lang">\n\t\t\t\t<div class="dropdown toggle">\n\t\t\t\t\t<input id="t1" type="checkbox" unchecked>\n\t\t\t\t\t<label for="t1">langage</label>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="index.html">English</a></li>\n\t\t\t\t\t\t<li><a href="index_fr.html">Francais</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="appetizer">\n\t\t\t<div class="text">\n\t\t\t\t<h1>Découvre la durabilité sur campus !</h>\n\t\t\t\t\t<p>Il existe de nombreuses ressources et personnels disponibles pour les étudiants sur le campus de l'EPFL en matière de développement durable. Ce site Internet, construit par des étudiants (Mehdi El Bouari & Ke Li, 2023), a pour objectif de fournir une liste complète de ces ressources, et de les rendre facilement accessibles à tous.</p>\n\t\t\t\t\t<p>Pour entrer en contact avec l’équipe d’éducation au développement durable à propos de ce site ou pour d’autres raisons, n’hésitez pas à contacter <a href="mailto:sustainability@epfl.ch">sustainability@epfl.ch</a> pour plus d’informations!\n\t\t\t\t\t</p>\n\t\t\t</div>\n\t\t\t<div class="subbubble-container" id="subbubbles">\n\t\t\t\t<div class="midcontainer" id="upper_subbubbles">\n"""
    return start

# generate the sub-bubbles
def generate_subbubbles(language, cat_len):
    subbubbles = ""
    if language == "en":
        category_name = "Category Name en"
    else:
        category_name = "Category Name fr"
    
    # generate upper sub-bubbles
    for i in range(math.ceil(cat_len/2)):
        subbubbles += f"""\t\t\t\t\t<div class="sub-bubble" id="subbubble{i+1}">\n\t\t\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t\t\t<span>{categories[category_name][i]}</span>\n\t\t\t\t\t</div>\n"""
    subbubbles += """\t\t\t\t</div>\n\t\t\t\t<div class="midcontainer" id="lower_subbubbles">\n"""
    
    # generate lower sub-bubbles
    for i in range(math.ceil(cat_len/2),cat_len):
        subbubbles += f"""\t\t\t\t\t<div class="sub-bubble" id="subbubble{i+1}">\n\t\t\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t\t\t<span>{categories[category_name][i]}</span>\n\t\t\t\t\t</div>\n"""
    subbubbles += """\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="arrow" id="arrow">\n\t\t\t<svg id="more-arrows">\n\t\t\t\t<polygon class="arrow-top" points="18.8,13.95 0.9,0.65 1.65,0 18.8,12.65 35.95,0 36.85,0.65 " />\n\t\t\t\t<polygon class="arrow-middle" points="18.8,22.9 0.4,9.35 2.2,8.2 18.8,20.6 35.6,8.2 37.25,9.35" />\n\t\t\t\t<polygon class="arrow-bottom" points="18.8,32 0,18.05 2.55,16.4 18.8,28.4 35.2,16.4 37.75,18.05" />\n\t\t\t</svg>\n\t\t</div>\n\t</div>\n\t<div class="container" id="content">\n"""

    return subbubbles

# generate the detailed bubbles
def generate_detailed_bubbles(language, cat_len,categories, resources):
    if language == "en":
        category_name = "Category Name en"
        resource_content = "English content"
        resource_image = "Image eng"
    else:
        category_name = "Category Name fr"
        resource_content = "French content"
        resource_image = "Image fr"
    
    j = 0
    # generate the upper bubbles
    detailed_bubbles = f"""\t\t<div class="midcontainer" id="upper-bubbles">\n"""
    for i in range(math.ceil(cat_len/2)):
        #add comment
        detailed_bubbles += f"""\t\t\t<!-- Category {i+1}: {categories[category_name][i]} -->\n"""
        #add bubble
        detailed_bubbles += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t<span>{categories[category_name][i]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources["Category"][j] == i+1:
            # add comment
            detailed_bubbles += f"""\t\t\t\t<!-- Resource {j+1}: {resources["Name"][j]} -->\n"""
            # add resource img
            detailed_bubbles += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources["Link"][j]}">\n\t\t\t\t\t\t<img src="logo\{resources[resource_image][j]}" alt="{resources["Name"][j]}">\n\t\t\t\t\t</a>\n"""
            # add resource description
            detailed_bubbles += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources["Name"][j]}</h3>\n\t\t\t\t\t\t{resources[resource_content][j]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
            j += 1
            if j == len(resources):
                break
        # end the bubble
        detailed_bubbles += f"""\t\t\t</div>\n"""

    # end the upper bubbles
    detailed_bubbles += f"""\t\t</div>\n"""

    # generate the lower bubbles
    detailed_bubbles += f"""\t\t<div class="midcontainer" id="lower-bubbles">\n"""
    for i in range(math.ceil(cat_len/2),cat_len):
        #add comment
        detailed_bubbles += f"""\t\t\t<!-- Category {i+1}: {categories[category_name][i]} -->\n"""
        #add bubble
        detailed_bubbles += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t<span>{categories[category_name][i]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources["Category"][j] == i+1:
            # add comment
            detailed_bubbles += f"""\t\t\t\t<!-- Resource {j+1}: {resources["Name"][j]} -->\n"""
            # add resource img
            detailed_bubbles += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources["Link"][j]}">\n\t\t\t\t\t\t<img src="logo\{resources[resource_image][j]}" alt="{resources["Name"][j]}">\n\t\t\t\t\t</a>\n"""
            # add resource description
            detailed_bubbles += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources["Name"][j]}</h3>\n\t\t\t\t\t\t{resources[resource_content][j]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
            j += 1
            if j == len(resources):
                break
        # end the bubble
        detailed_bubbles += f"""\t\t\t</div>\n"""
    
    # end the lower bubbles
    detailed_bubbles += f"""\t\t</div>\n"""

    return detailed_bubbles

# end the html
def generate_end():
    # end the body
    end = f"""\t</div>"""

    # the javascript part
    end += """\t<script>\n\t\t$(document).click(function (event) {\n\t\t\tif (\n\t\t\t\t$('.toggle > input').is(':checked') &&\n\t\t\t\t!$(event.target).parents('.toggle').is('.toggle')\n\t\t\t) {\n\t\t\t\t$('.toggle > input').prop('checked', false);\n\t\t\t}\n\t\t})\n\t</script>\n\t<script>\n\t\t// Get a reference to the button and the target container\n\t\tconst scrollButton = document.getElementById('arrow');\n\t\tconst scrollButton2 = document.getElementById('subbubbles');\n\t\tconst targetContainer = document.getElementById('content');\n\n\t\t// Add a click event listener to the button\n\t\tscrollButton.addEventListener('click', function () {\n\t\t\t// Scroll to the target container smoothly\n\t\t\ttargetContainer.scrollIntoView({ behavior: 'smooth' });\n\t\t});\n\t\t// Add a click event listener to the button\n\t\tscrollButton2.addEventListener('click', function () {\n\t\t\t// Scroll to the target container smoothly\n\t\t\ttargetContainer.scrollIntoView({ behavior: 'smooth' });\n\t\t});\n\t</script>\n\t<script>\n\t\t$(document).ready(function () {\n\t\t\t// Wait for the page to fully load\n\n\t\t\t// Get the height of container1\n\t\t\tvar container1Height = $('#container1').height();\n\n\t\t\t// Set the height of container2 to match container1\n\t\t\t$('#container2').height(container1Height);\n\t\t});\n\t</script>\n\t<script src="position_computation.js"></script>\n</body>\n\n</html>\n\n"""
    return end

if __name__ == "__main__":
    # read the tsv file
    categories = pd.read_csv("Descriptions - Categories.tsv", sep="\t")
    resources = pd.read_csv("Descriptions - ressources.tsv", sep="\t")
    cat_len= len(categories)

    # generate the english html
    html_en = generate_start("en")
    # generate sub-bubbles
    html_en += generate_subbubbles("en", cat_len)
    # generate the detailed bubbles
    html_en += generate_detailed_bubbles("en", cat_len, categories, resources)
    # end the html
    html_en += generate_end()
    # write the html file
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_en)
    

    # generate the french html
    html_fr = generate_start("fr")
    # generate sub-bubbles
    html_fr += generate_subbubbles("fr", cat_len)
    # generate the detailed bubbles
    html_fr += generate_detailed_bubbles("fr", cat_len, categories, resources)
    # end the html
    html_fr += generate_end()
    # write the html file
    with open("index_fr.html", "w", encoding="utf-8") as f:
        f.write(html_fr)