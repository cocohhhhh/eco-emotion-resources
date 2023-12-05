# Read the category and the related resources from the tsv file
# generate a html from that

from csv import DictReader
import math

#generate css start
def generate_css_start():
    css="""body {\n  background-color: #ffffc5;\n  margin: 0;\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  flex-direction: column;\n  overflow-y: scroll;\n  overflow-x: hidden;\n}\n\n/* #region font definition*/\n@font-face {\n  font-family: 'SuisseIntl';\n  src: url('font/SuisseIntl-Medium.otf') format('opentype');\n  font-weight: normal;\n  font-style: normal;\n}\n\n@font-face {\n  font-family: 'SuisseIntlLight';\n  src: url('font/SuisseIntl-Light.otf') format('opentype');\n  font-weight: normal;\n  font-style: normal;\n}\n\n/* #endregion */\n\n/* #region Introductory page */\n\n.container {\n  background-color: transparent;\n  display: flex;\n  width: 100%;\n  height: auto;\n  flex-direction: column;\n  overflow: hidden;\n  justify-content: space-between;\n}\n\n.upper_part {\n  display: flex;\n  width: 100%;\n  height: 90%;\n  flex-direction: column;\n  justify-content: center;\n  align-items: center;\n}\n\n#intro {\n  flex-direction: column;\n  height: fit-content;\n  min-height: 100vh;\n  background: linear-gradient(#47d9e9, transparent 100%);\n  justify-content: top;\n  align-items: center;\n}\n\n#subbubbles {\n  display: none;\n}\n\n.banner {\n  position: relative;\n  top: 0%;\n  width: 90%;\n  height: auto;\n  display: flex;\n  align-items: center;\n  Justify-content: space-between;\n  font-weight: bold;\n  font-family: 'SuisseIntl';\n  color: #000;\n  border-bottom: 1px solid #000;\n  z-index: 1;\n}\n\n.banner .title {\n  font-size: 16px;\n  font-weight: bold;\n  font-family: 'SuisseIntl';\n  width: 60%;\n}\n\n.banner .lang {\n  display: flex;\n  justify-content: flex-end;\n  width: 115px;\n}\n\n.appetizer {\n  position: relative;\n  width: 90%;\n  height: 90%;\n  display: flex;\n  justify-content: space-between;\n  flex-direction: row;\n  font-size: large;\n  color: #000;\n}\n\n.appetizer .text {\n  width: 100%;\n  height: 100%;\n}\n\n.appetizer .text h1 {\n  font-size: 32px;\n  font-weight: bold;\n  font-family: 'SuisseIntl';\n}\n\n.appetizer .text p {\n  margin-top: 3%;\n  font-size: 20px;\n  font-family: 'SuisseIntlLight';\n}\n\n.appetizer .image img {\n  display: none;\n}\n\n/* #endregion*/\n\n/* #region Arrow & Hover Animation */\n.arrow {\n  position: relative;\n  margin-bottom: 15%;\n}\n\n.arrow-top {\n  display: none;\n}\n\n.arrow-middle {\n  display: none;\n}\n\n.arrow p {\n  margin: 0 0 20px;\n}\n\n#more-arrows {\n  width: 37.5px;\n  height: 32.5px;\n}\n\n#more-arrows:hover polygon {\n  fill: black;\n  transition: all .2s ease-out;\n}\n\n#more-arrows:hover polygon.arrow-bottom {\n  transform: translateY(-9px);\n}\n\n#more-arrows:hover polygon.arrow-top {\n  transform: translateY(9px);\n}\n\npolygon {\n  fill: black;\n  transition: all .2s ease-out;\n}\n\npolygon.arrow-middle {\n  opacity: 0.75;\n}\n\npolygon.arrow-top {\n  opacity: 0.5;\n}\n\n/* #endregion End for arrows */\n\n/* #region language dropdown */\n.dropdown {\n  width: 100%;\n  display: inline-block;\n  position: relative;\n  margin-bottom: -5px;\n  font-size: 18px;\n}\n\n.dropdown.toggle>input {\n  display: none;\n}\n\n.dropdown>a,\n.dropdown.toggle>label {\n  border-radius: 2px;\n}\n\n.dropdown>a::after,\n.dropdown.toggle>label::after {\n  content: "";\n  float: right;\n  margin: 15px 15px 0 0;\n  width: 0;\n  height: 0;\n  border-left: 5px solid transparent;\n  border-right: 5px solid transparent;\n  border-top: 10px solid black;\n}\n\n.dropdown ul {\n  list-style-type: none;\n  display: block;\n  margin: 0;\n  padding: 0;\n  position: absolute;\n  width: 100%;\n  box-shadow: 0 6px 5px -5px rgba(0, 0, 0, 0.3);\n  overflow: hidden;\n}\n\n.dropdown a,\n.dropdown.toggle>label {\n  display: block;\n  padding: 0 0 0 10px;\n  text-decoration: none;\n  line-height: 40px;\n  font-size: 13px;\n  text-transform: uppercase;\n  font-weight: bold;\n  color: black;\n  background-color: transparent;\n}\n\n.dropdown li {\n  height: 0;\n  overflow: hidden;\n  transition: all 500ms;\n\n}\n\n.dropdown.hover li {\n  transition-delay: 300ms;\n}\n\n.dropdown li:first-child a {\n  border-radius: 2px 2px 0 0;\n}\n\n.dropdown li:last-child a {\n  border-radius: 0 0 2px 2px;\n}\n\n.dropdown a:hover,\n.dropdown.toggle>label:hover,\n.dropdown.toggle>input:checked~label {\n  background-color: transparent;\n  color: #f5f5f5;\n}\n\n.dropdown.toggle>label:hover::after,\n.dropdown.toggle>input:checked~label::after {\n  border-top-color: #f5f5f5;\n}\n\n.dropdown.toggle>input:checked~ul li {\n  height: 35px;\n}\n\n/* #endregion End for Custom dropdown */\n\n/* #region Bubbles*/\n\n#content {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  flex-direction: column;\n  height: fit-content;\n}\n\n.midcontainer {\n  justify-content: center;\n  align-items: center space-between;\n  width: 100%;\n  height: auto;\n}\n\n.bubble {\n  margin-left: 4%;\n  margin-right: 4%;\n  position: relative;\n  width: 92%;\n  height: auto;\n  aspect-ratio: 1/1;\n  border-radius: 50%;\n  cursor: pointer;\n  display: flex;\n  flex-direction: column;\n  justify-content: center;\n  align-items: center;\n  z-index: 2;\n}\n\n.bubble img {\n  position: relative;\n  max-width: 30%;\n  max-height: 30%;\n  object-fit: contain;\n  z-index: 2;\n}\n\n.bubble span {\n  width: 50%;\n  text-align: center;\n  position: relative;\n  font-size: 18px;\n  object-fit: contain;\n  font-family: 'SuisseIntl';\n  z-index: 2;\n  font-weight: 700;\n}\n\n.border {\n  position: absolute;\n  width: 100%;\n  height: 100%;\n  border-radius: 50%;\n  z-index: 1;\n}\n\n.bubble + .bubble {\n  margin-top: 30px;\n}\n\n.midcontainer + .midcontainer {\n  margin-top: 30px;\n}\n\n.smaller {\n  position: absolute;\n  width: 24%;\n  height: 16%;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  z-index: 2;\n}\n\n.smaller a {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  flex-direction: column;\n  width: 100%;\n  height: 100%;\n  text-decoration: none;\n  color: #000;\n}\n\n.smaller a span {\n  text-decoration: none;\n  color: #000;\n  font-family: "SuisseIntl";\n  font-size: 15px;\n  text-align: center;\n}\n\n.smaller img {\n  max-width: 100%;\n  max-height: 100%;\n  object-fit: contain;\n}\n\n.text-description {\n  position: absolute;\n  padding: 7px;\n  background-color: #000;\n  color: #fff;\n  border-radius: 5px;\n  white-space: normal;\n  width: 500%;\n  visibility: hidden;\n  opacity: 0;\n  z-index: 1;\n  text-align: left;\n  font-family: 'SuisseIntl';\n  transition: opacity 0.2s ease;\n}\n\n.text-description h3 {\n  margin: 0;\n  font-family: 'SuisseIntl';\n  font-size: 18px;\n  color: #fff;\n  margin-bottom: 5px;\n  text-align: center;\n}\n\n/* #endregion */\n\n@media only screen and (min-width: 1150px) {\n\n  /* For Desktops: */\n  body {\n\theight: 200vh;\n  }\n\n  html {\n\tscroll-snap-type: y mandatory;\n  }\n\n  /* #region Arrow & Hover Animation */\n  .arrow {\n\tdisplay: block;\n\tposition: absolute;\n\tmargin-bottom: 0px;\n\tleft: 50%;\n\ttop: 90%;\n\ttransform: translate(-50%, -50%);\n  }\n\n  .arrow-top {\n\tdisplay: block;\n  }\n\n  .arrow-middle {\n\tdisplay: block;\n  }\n\n  /* #endregion End for arrows */\n\n  .container {\n\twidth: 100%;\n\theight: 50% !important;\n\tscroll-snap-align: start;\n\tscroll-snap-stop: always;\n  }\n\n  .banner {\n\theight: 9%;\n\talign-items: end;\n  }\n\n  .banner .title {\n\tfont-size: 32px;\n  }\n\n  .banner .lang {\n\tdisplay: flex;\n\tjustify-content: flex-end;\n  }\n\n  .appetizer {\n\ttop: 1%;\n  }\n\n  .appetizer .text {\n\twidth: 35%;\n\theight: 100%;\n  }\n\n  #subbubbles {\n\tdisplay: block;\n\twidth: 60%;\n\theight: 80%;\n\tmargin-top: 1%;\n\talign-items: center;\n\tjustify-content: center;\n  }\n\n  .sub-bubble {\n\tposition: relative;\n\theight: 90%;\n\taspect-ratio: 1/1;\n\tborder-radius: 50%;\n\tcursor: pointer;\n\tdisplay: flex;\n\tflex-direction: column;\n\tjustify-content: center;\n\talign-items: center;\n\tbackground-color: #fff;\n\tfont-family: "SuisseIntl";\n\tfont-size: 20px;\n\tfont-weight: 700;\n  }\n\n  .sub-bubble img {\n\tposition: relative;\n\tmax-width: 40%;\n\tmax-height: 40%;\n\tobject-fit: contain;\n  }\n\n  .sub-bubble span {\n\twidth: 70%;\n\ttext-align: center;\n\tposition: relative;\n\tfont-size: 18px;\n\tobject-fit: contain;\n\tfont-family: 'SuisseIntl';\n\tfont-weight: 700;\n  }\n\n  .midcontainer {\n\tdisplay: flex;\n\tjustify-content: space-around;\n\talign-items: center;\n\tflex-direction: row;\n\twidth: 100%;\n\theight: 50%;\n  }\n\n  #upper_subbubbles {\n\talign-items: end;\n  justify-content: right;\n  }\n\n  #lower_subbubbles {\n    align-items: start;\n    justify-content: left;\n  }\n\n  .sub-bubble + .sub-bubble {\n\tmargin-left: 3.5%;\n  }\n\n\n  #upper-bubbles {\n\tposition: absolute;\n\ttop: 103%;\n\talign-items: end;\n  margin-right: 5%;\n  justify-content: right;\n  }\n\n  #lower-bubbles {\n\tposition: absolute;\n\ttop: 147%;\n\tjustify-content: left;\n\talign-items: start;\n  margin-left: 4%;\n  }\n\n  .bubble + .bubble {\n    margin-left: 4%;\n    }\n\n  .bubble {\n\tmargin-left: 0px;\n\tmargin-right: 0px;\n\theight: 100%;\n\twidth: auto;\n\taspect-ratio: 1;\n  }\n\n  .bubble + .bubble {\n\tmargin-top: 0px;\n  }\n\n  .midcontainer + .midcontainer {\n\tmargin-top: 0px;\n  }\n\n  .bubble:hover {\n\ttransition: background-color 0.2s ease;\n\tz-index: 3;\n  }\n\n\n  .smaller {\n\twidth: 30%;\n\theight: 20%;\n  }\n\n  .smaller img {\n\ttransform: scale(0.8);\n\tfilter: opacity(0.5);\n  }\n\n  .smaller img:hover {\n\ttransform: scale(1.5);\n\tfilter: opacity(1);\n\ttransition: all 0.2s ease;\n\tz-index: 3;\n  }\n\n  .text-description {\n\tposition: absolute;\n\tpadding: 7px;\n\tcolor: #000;\n\tborder-radius: 5px;\n\twhite-space: normal;\n\twidth: 400px;\n\tvisibility: hidden;\n\topacity: 0;\n\tz-index: 1;\n\ttext-align: left;\n\tfont-family: 'SuisseIntl';\n\ttransition: opacity 0.2s ease;\n  }\n\n  .text-description h3 {\n\tmargin: 0;\n\tfont-family: 'SuisseIntl';\n\tfont-size: 18px;\n\tcolor: #000;\n\tmargin-bottom: 5px;\n\ttext-align: center;\n  }\n\n  .smaller:hover .text-description {\n\tvisibility: visible;\n\topacity: 1;\n\tz-index: 3;\n  }\n\n  .text-description:hover {\n\tdisplay: none;\n  }\n\n}\n"""
    return css

# generate css colors
def generate_css_colors(len_cat, categories):
    css = ""
    for i in range(len_cat):
        if i<math.ceil(len_cat/2):
            pos_y="top: 0%;"
            if i<math.floor(len_cat/4):
                pos_x="left: 125%;"
            else:
                pos_x="right: 125%;"
        else:
            pos_y="bottom: 0%;"
            if i<math.ceil(len_cat/4+len_cat/2):
                pos_x="left: 125%;"
            else:
                pos_x="right: 125%;"
        css += f"""\n/*category{i+1}*/\n#subbubble{i+1} {{\n\tbackground: radial-gradient(circle farthest-side,{categories[i]["Bubble Color"]}, #ffffc5);\n}}\n\n#border{i+1} {{\n\tbackground: radial-gradient(circle farthest-side, {categories[i]["Bubble Color"]}, transparent 100%);\n}}\n\n#bubble{i+1} .text-description {{\n\tbackground-color: {categories[i]["Description Color"]};\n\t{pos_x}\n\t{pos_y}\n\n}}"""
    return css

# generate the start
def generate_start(language):
    if language == "en":
        start = """<!DOCTYPE html>\n<html>\n\n<head>\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-N7RECYYB7G"></script>\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\tfunction gtag(){dataLayer.push(arguments);}\n\t\tgtag('js', new Date());\n\t\tgtag('config', 'G-N7RECYYB7G');\n\t</script>\n\t<title>EPFL Sustainability Resources</title>\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n\t<link rel="icon" href="logo\Durabilite.png">\n</head>\n\n<body>\n\t<div class="container" id="intro">\n\t\t<div class="upper_part">\n\t\t<div class="banner">\n\t\t\t<div class="title">\n\t\t\t\tEPFL Sustainability Resources\n\t\t\t</div>\n\t\t\t<div class="lang">\n\t\t\t\t<div class="dropdown toggle">\n\t\t\t\t\t<input id="t1" type="checkbox" unchecked>\n\t\t\t\t\t<label for="t1">language</label>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="index.html">English</a></li>\n\t\t\t\t\t\t<li><a href="index_fr.html">Francais</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="appetizer">\n\t\t\t<div class="text">\n\t\t\t\t<h1>Discover sustainability on your campus!</h>\n\t\t\t\t\t<p>There are many resources & staff available for students on EPFL campus regarding sustainability.\n\t\t\t\t\t\tThis website, built by students <i>(Mehdi El Bouari & Ke Li, 2023)</i>, aims to provide a\n\t\t\t\t\t\tcomprehensive\n\t\t\t\t\t\tlist of these resources, and to make them easily accessible to all.\n\t\t\t\t\t</p>\n\t\t\t\t\t<p>To get in touch with the sustainability education team about this site or for other reasons,\n\t\t\t\t\t\tdon’t\n\t\t\t\t\t\thesitate to contact <a href="mailto:sustainability@epfl.ch">sustainability@epfl.ch</a> for\n\t\t\t\t\t\tmore information!\n\t\t\t\t\t</p>\n\t\t\t</div>\n\t\t\t<div class="subbubble-container" id="subbubbles">\n\t\t\t\t<div class="midcontainer" id="upper_subbubbles">\n"""
    else:
        start = """<!DOCTYPE html>\n<html>\n\n<head>\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-N7RECYYB7G"></script>\n\t<script>\n\t\twindow.dataLayer = window.dataLayer || [];\n\t\tfunction gtag(){dataLayer.push(arguments);}\n\t\tgtag('js', new Date());\n\t\tgtag('config', 'G-N7RECYYB7G');\n\t</script>\n\t<title>EPFL Sustainability Resources</title>\n\t<meta name="viewport" content="width=device-width, initial-scale=1">\n\t<link rel="stylesheet" href="style.css">\n\t<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n\t<link rel="icon" href="logo\Durabilite.png">\n</head>\n\n<body>\n\t<div class="container" id="intro">\n\t\t<div class="upper_part">\n\t\t<div class="banner">\n\t\t\t<div class="title">\n\t\t\t\tEPFL Ressources durables\n\t\t\t</div>\n\t\t\t<div class="lang">\n\t\t\t\t<div class="dropdown toggle">\n\t\t\t\t\t<input id="t1" type="checkbox" unchecked>\n\t\t\t\t\t<label for="t1">langage</label>\n\t\t\t\t\t<ul>\n\t\t\t\t\t\t<li><a href="index.html">English</a></li>\n\t\t\t\t\t\t<li><a href="index_fr.html">Francais</a></li>\n\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="appetizer">\n\t\t\t<div class="text">\n\t\t\t\t<h1>Découvre la durabilité sur campus !</h>\n\t\t\t\t\t<p>Il existe de nombreuses ressources et personnels disponibles pour les étudiants sur le campus de l'EPFL en matière de développement durable. Ce site Internet, construit par des étudiants (Mehdi El Bouari & Ke Li, 2023), a pour objectif de fournir une liste complète de ces ressources, et de les rendre facilement accessibles à tous.</p>\n\t\t\t\t\t<p>Pour entrer en contact avec l’équipe d’éducation au développement durable à propos de ce site ou pour d’autres raisons, n’hésitez pas à contacter <a href="mailto:sustainability@epfl.ch">sustainability@epfl.ch</a> pour plus d’informations!\n\t\t\t\t\t</p>\n\t\t\t</div>\n\t\t\t<div class="subbubble-container" id="subbubbles">\n\t\t\t\t<div class="midcontainer" id="upper_subbubbles">\n"""
    return start

# generate the sub-bubbles
def generate_subbubbles(language, cat_len, categories):
    subbubbles = ""
    if language == "en":
        category_name = "Category Name en"
    else:
        category_name = "Category Name fr"
    
    # generate upper sub-bubbles
    for i in range(math.ceil(cat_len/2)):
        subbubbles += f"""\t\t\t\t\t<div class="sub-bubble" id="subbubble{i+1}">\n\t\t\t\t\t\t<img src="logo\{categories[i]["Image"]}" alt="Image">\n\t\t\t\t\t\t<span>{categories[i][category_name]}</span>\n\t\t\t\t\t</div>\n"""
    subbubbles += """\t\t\t\t</div>\n\t\t\t\t<div class="midcontainer" id="lower_subbubbles">\n"""
    
    # generate lower sub-bubbles
    for i in range(math.ceil(cat_len/2),cat_len):
        subbubbles += f"""\t\t\t\t\t<div class="sub-bubble" id="subbubble{i+1}">\n\t\t\t\t\t\t<img src="logo\{categories[i]["Image"]}" alt="Image">\n\t\t\t\t\t\t<span>{categories[i][category_name]}</span>\n\t\t\t\t\t</div>\n"""
    subbubbles += """\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t</div>\n\t\t<div class="arrow" id="arrow">\n\t\t\t<svg id="more-arrows">\n\t\t\t\t<polygon class="arrow-top" points="18.8,13.95 0.9,0.65 1.65,0 18.8,12.65 35.95,0 36.85,0.65 " />\n\t\t\t\t<polygon class="arrow-middle" points="18.8,22.9 0.4,9.35 2.2,8.2 18.8,20.6 35.6,8.2 37.25,9.35" />\n\t\t\t\t<polygon class="arrow-bottom" points="18.8,32 0,18.05 2.55,16.4 18.8,28.4 35.2,16.4 37.75,18.05" />\n\t\t\t</svg>\n\t\t</div>\n\t</div>\n\t<div class="container" id="content">\n"""

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
        detailed_bubbles += f"""\t\t\t<!-- Category {i+1}: {categories[i][category_name]} -->\n"""
        #add bubble
        detailed_bubbles += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories[i]["Image"]}" alt="Image">\n\t\t\t\t<span>{categories[i][category_name]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources[j]["Category"] == str(i+1):
            # add comment
            detailed_bubbles += f"""\t\t\t\t<!-- Resource {j+1}: {resources[j]["Name"]} -->\n"""
            # add resource img
            detailed_bubbles += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources[j]["Link"]}">\n\t\t\t\t\t\t<img src="logo\{resources[j][resource_image]}" alt="{resources[j]["Name"]}">\n\t\t\t\t\t</a>\n"""
            # add resource description
            detailed_bubbles += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources[j]["Name"]}</h3>\n\t\t\t\t\t\t{resources[j][resource_content]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
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
        detailed_bubbles += f"""\t\t\t<!-- Category {i+1}: {categories[i][category_name]} -->\n"""
        #add bubble
        detailed_bubbles += f"""\t\t\t<div class="bubble" id="bubble{i+1}">\n\t\t\t\t<img src="logo\{categories[i]["Image"]}" alt="Image">\n\t\t\t\t<span>{categories[i][category_name]}</span>\n\t\t\t\t<div class="border" id="border{i+1}"></div>\n"""
        #add resources
        while resources[j]["Category"] == str(i+1):
            # add comment
            detailed_bubbles += f"""\t\t\t\t<!-- Resource {j+1}: {resources[j]["Name"]} -->\n"""
            # add resource img
            detailed_bubbles += f"""\t\t\t\t<div class="bubble smaller" id="resource{j+1}">\n\t\t\t\t\t<a href="{resources[j]["Link"]}">\n\t\t\t\t\t\t<img src="logo\{resources[j][resource_image]}" alt="{resources[j]["Name"]}">\n\t\t\t\t\t</a>\n"""
            # add resource description
            detailed_bubbles += f"""\t\t\t\t\t<div class="text-description">\n\t\t\t\t\t\t<h3>{resources[j]["Name"]}</h3>\n\t\t\t\t\t\t{resources[j][resource_content]}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"""
            j += 1
            if j == len(resources):                
                detailed_bubbles += f"""\t\t\t</div>\n"""
                detailed_bubbles += f"""\t\t</div>\n"""
                return detailed_bubbles
            
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
    print("Generating html...")

    with open("Descriptions - Categories.tsv", "r", encoding="utf-8") as f:
        categories = DictReader(f, delimiter="\t")
        categories = list(categories)
    
    cat_len= len(categories)

    with open("Descriptions - ressources.tsv", "r", encoding="utf-8") as f:
        resources = DictReader(f, delimiter="\t")
        resources = list(resources)

    # generate the english html
    html_en = generate_start("en")
    # generate sub-bubbles
    html_en += generate_subbubbles("en", cat_len, categories)
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
    html_fr += generate_subbubbles("fr", cat_len, categories)
    # generate the detailed bubbles
    html_fr += generate_detailed_bubbles("fr", cat_len, categories, resources)
    # end the html
    html_fr += generate_end()
    # write the html file
    with open("index_fr.html", "w", encoding="utf-8") as f:
        f.write(html_fr)
    
    print("Html generated!")
    
    # generate the css file
    css = generate_css_start()
    css += generate_css_colors(cat_len, categories)
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)