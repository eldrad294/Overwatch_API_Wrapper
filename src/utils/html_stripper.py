def html_stripper(content):
    """ Receives html document and removes any html elements inside it """
    #
    content = str(content)
    html_elements = ["<br>", "<br/>", "<br />", "<p>", "</p>", "<h1>", "</h1>", "<h2>", "</h2>", "<ul>", "</ul>",
                     "<li>", "</li>", "<strong>", "</strong>", "<a>", "</a>", "<a href=", "target=", "\"_blank", "\">"]
    for element in html_elements:
        if element in ["<br>", "<br/>", "<br />"]:
            content = content.replace(element, "\n")
        else:
            content = content.replace(element, "")
    #
    return content
