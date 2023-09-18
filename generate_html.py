# Read the category and the related resources from the tsv file
# generate a html from that

import pandas as pd

if __name__ == "__main__":
    # read the tsv file
    categories = pd.read_csv("Descriptions - Categories.tsv", sep="\t")
    resources = pd.read_csv("Descriptions - ressources.tsv", sep="\t")

    # generate the html
    html = """<!DOCTYPE html>\n<html>\n\n<head>\n\t<title>EPFL Sustainability Resources</title>\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n\t<link rel="icon" href="logo\Durabilite.png">\n</head>\n\n<body>\n\t<div class="container" id="intro">\n\t\t<div class="banner">\n\t\t\t<div class="title">\n\t\t\t\tEPFL Sustainability Resources\n\t\t\t</div>\n\t\t\t<div class="lang">\n\t\t\t\t<div class="dropdown toggle">\n\t\t\t\t\t<input id="t1" type="checkbox" unchecked>\n\t\t\t\t\t<label for="t1">language</label>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="index.html">English</a></li>\n\t\t\t\t\t\t<li><a href="index_fr.html">Francais</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="appetizer">\n\t\t\t<div class="text">\n\t\t\t\t<h1>Discover sustainability on your campus!</h>\n\t\t\t\t\t<p>There are many resources & staff available for students on EPFL campus regarding sustainability.\n\t\t\t\t\t\tThis website, built by students <i>(Mehdi El Bouari & Ke Li, 2023)</i>, aims to provide a\n\t\t\t\t\t\tcomprehensive\n\t\t\t\t\t\tlist of these resources, and to make them easily accessible to all.\n\t\t\t\t\t</p>\n\t\t\t\t\t<p>To get in touch with the sustainability education team about this site or for other reasons,\n\t\t\t\t\t\tdon’t\n\t\t\t\t\t\thesitate to contact <a href="mailto:sustainability@epfl.ch">sustainability@epfl.ch</a> for\n\t\t\t\t\t\tmore information!\n\t\t\t\t\t</p>\n\t\t\t</div>\n\t\t\t<div class="subbubble-container" id="subbubbles">\n\t\t\t\t<div class="midcontainer" id="upper_subbubbles">\n\t\t\t\t\t<div class="sub-bubble" id="subbubble1">\n\t\t\t\t\t\t<img src="logo\Apprendre.png" alt="Image">\n\t\t\t\t\t\t<span>Inform Yourself</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="sub-bubble" id="subbubble2">\n\t\t\t\t\t\t<img src="logo\Services.png" alt="Image">\n\t\t\t\t\t\t<span>Enjoy Services</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="sub-bubble" id="subbubble3">\n\t\t\t\t\t\t<img src="logo\Community.png" alt="Image">\n\t\t\t\t\t\t<span>Take Action</span>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t\t<div class="midcontainer" id="lower_subbubbles">\n\t\t\t\t\t<div class="sub-bubble" id="subbubble4">\n\t\t\t\t\t\t<img src="logo\Startup.png" alt="Image">\n\t\t\t\t\t\t<span>Launch</span>\n\t\t\t\t\t\t<span>Your Project</span>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class="sub-bubble" id="subbubble5">\n\t\t\t\t\t\t<img src="logo\Sain.png" alt="Image">\n\t\t\t\t\t\t<span>Take Care</span>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="arrow" id="arrow">\n\t\t\t<svg id="more-arrows">\n\t\t\t\t<polygon class="arrow-top" points="18.8,13.95 0.9,0.65 1.65,0 18.8,12.65 35.95,0 36.85,0.65 " />\n\t\t\t\t<polygon class="arrow-middle" points="18.8,22.9 0.4,9.35 2.2,8.2 18.8,20.6 35.6,8.2 37.25,9.35" />\n\t\t\t\t<polygon class="arrow-bottom" points="18.8,32 0,18.05 2.55,16.4 18.8,28.4 35.2,16.4 37.75,18.05" />\n\t\t\t</svg>\n\t\t</div>\n\t</div>\n\t<div class="container" id="content">\n"""

    j = 0
    # generate the upper bubbles
    html += f"""\t\t<div class="midcontainer" id="upper-bubbles">\n"""
    for i in range(3):
        #add comment
        html += f"""<!-- Category {i+1}: {categories["Category Name"][i]} -->"""
        #add bubble
        html += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t<span>{categories["Category Name"][i]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources["Category"][j] == i+1:
            # add comment
            html += f"""<!-- Resource {j+1}: {resources["Name"][j]} -->"""
            # add resource img
            html += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources["Link"][j]}"><img src="logo\{resources["Image eng"][j]}" alt="{resources["Name"][j]}"></a>\n\t\t\t\t\n"""
            # add resource description
            html += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources["Name"][j]}</h3>\n\t\t\t\t\t\t{resources["English content"][j]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
            j += 1
            if j == len(resources):
                break
        # end the bubble
        html += f"""\t\t\t</div>\n"""
    
    # end the upper bubbles
    html += f"""\t\t</div>\n"""

    # generate the lower bubbles
    html += f"""\t\t<div class="midcontainer" id="lower-bubbles">\n"""
    for i in range(3,5):
        #add comment
        html += f"""<!-- Category {i+1}: {categories["Category Name"][i]} -->"""
        #add bubble
        html += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories["Image"][i]}" alt="Image">\n\t\t\t\t<span>{categories["Category Name"][i]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources["Category"][j] == i+1:
            # add comment
            html += f"""<!-- Resource {j+1}: {resources["Name"][j]} -->"""
            # add resource img
            html += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources["Link"][j]}"><img src="logo\{resources["Image eng"][j]}" alt="{resources["Name"][j]}"></a>\n\t\t\t\t\n"""
            # add resource description
            html += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources["Name"][j]}</h3>\n\t\t\t\t\t\t{resources["English content"][j]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
            j += 1
            if j == len(resources):
                break
        # end the bubble
        html += f"""\t\t\t</div>\n"""
    
    # end the lower bubbles
    html += f"""\t\t</div>\n"""

    # end the body
    html += f"""\t</div>"""

    # the javascript part
    html += """\t<script>\n\t\t$(document).click(function (event) {\n\t\t\tif (\n\t\t\t\t$('.toggle > input').is(':checked') &&\n\t\t\t\t!$(event.target).parents('.toggle').is('.toggle')\n\t\t\t) {\n\t\t\t\t$('.toggle > input').prop('checked', false);\n\t\t\t}\n\t\t})\n\t</script>\n\t<script>\n\t\t// Get a reference to the button and the target container\n\t\tconst scrollButton = document.getElementById('arrow');\n\t\tconst scrollButton2 = document.getElementById('subbubbles');\n\t\tconst targetContainer = document.getElementById('content');\n\n\t\t// Add a click event listener to the button\n\t\tscrollButton.addEventListener('click', function () {\n\t\t\t// Scroll to the target container smoothly\n\t\t\ttargetContainer.scrollIntoView({ behavior: 'smooth' });\n\t\t});\n\t\t// Add a click event listener to the button\n\t\tscrollButton2.addEventListener('click', function () {\n\t\t\t// Scroll to the target container smoothly\n\t\t\ttargetContainer.scrollIntoView({ behavior: 'smooth' });\n\t\t});\n\t</script>\n\t<script>\n\t\t$(document).ready(function () {\n\t\t\t// Wait for the page to fully load\n\n\t\t\t// Get the height of container1\n\t\t\tvar container1Height = $('#container1').height();\n\n\t\t\t// Set the height of container2 to match container1\n\t\t\t$('#container2').height(container1Height);\n\t\t});\n\t</script>\n\t<script src="position_computation.js"></script>\n</body>\n\n</html>\n\n"""

    # write the html file
    with open("index_auto.html", "w", encoding="utf-8") as f:
        f.write(html)
    